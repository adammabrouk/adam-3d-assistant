import yt_dlp

url = 'https://www.youtube.com/watch?v=anplUNnkM68'

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
video_title = info_dict['title']
video_name = "english_vid"
name = video_name
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'noplaylist': True,
    'continue_dl': True,
    'outtmpl': f'./{name}.wav',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'geobypass': True,
    'ffmpeg_location': '/opt/homebrew/bin/ffmpeg'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(url)
