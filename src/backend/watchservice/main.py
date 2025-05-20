import time
import queue
import os
import requests
from pprint import pprint  # Import pprint for pretty-printing JSON responses
from watchdog.observers.polling import (
    PollingObserver,
)  # Use PollingObserver for NFS compatibility
from watchdog.events import FileSystemEventHandler

# Configuration
DIRECTORY_TO_WATCH = "/mnt/truenas/amabrouk/backend/watchservice"
API_ENDPOINT = "http://127.0.0.1:8080/inference"
RETRY_DELAY = 10  # Delay in seconds before retrying a failed request

# Initialize a queue for files that need to be processed
file_queue = queue.Queue()


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Only consider files (not directories)
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            # Add the file path to the queue for processing
            file_queue.put(event.src_path)


def process_queue():
    while True:
        try:
            # Get a file path from the queue
            file_path = file_queue.get_nowait()
        except queue.Empty:
            # No file to process
            break

        try:
            # Post the file to the API endpoint using the requests library
            with open(file_path, "rb") as file_data:
                print(f"Sending file: {file_path}")
                response = requests.post(
                    API_ENDPOINT,
                    files={"file": file_data},
                    data={
                        "temperature": "0.0",
                        "temperature_inc": "0.2",
                        "response_format": "json",
                    },
                )
                response.raise_for_status()  # Raise an error for bad HTTP responses
                print(f"Successfully processed: {file_path}")
                print("Response:")
                pprint(response.json())  # Pretty-print the JSON response

        except requests.exceptions.RequestException as e:
            print(f"Failed to process {file_path}: {e}")
            # Requeue the file and wait before retrying
            file_queue.put(file_path)
            time.sleep(RETRY_DELAY)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")


def main():
    event_handler = FileHandler()
    observer = PollingObserver()  # Use PollingObserver for NFS
    observer.schedule(event_handler, path=DIRECTORY_TO_WATCH, recursive=True)
    observer.start()

    try:
        # Main loop to check and process the queue
        print("Watching for changes in directory: " + DIRECTORY_TO_WATCH)
        while True:
            process_queue()
            time.sleep(1)  # Sleep to avoid busy waiting
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
