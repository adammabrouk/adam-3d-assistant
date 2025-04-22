import torch
import librosa
import numpy as np
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import arabic_reshaper
from bidi.algorithm import get_display

# Check if MPS is available
device = torch.device("mps") if torch.backends.mps.is_built() and torch.backends.mps.is_available() else torch.device("cpu")

# Load model and processor
processor = AutoProcessor.from_pretrained("openai/whisper-small")
model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-small").to(device)

# Load audio file
audio_path = "english_vid.wav"
audio, sr = librosa.load(audio_path, sr=16000)

# Define batch size (10 seconds)
batch_size = 10 * sr

# Process audio in mini-batches
for i in range(0, len(audio), batch_size):
    batch = audio[i:i + batch_size]
    inputs = processor(batch, sampling_rate=sr, return_tensors="pt").to(device)
    
    with torch.no_grad():
        generated_ids = model.generate(inputs["input_features"])
        transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        # Reshape and display Arabic text correctly
        reshaped_text = arabic_reshaper.reshape(transcription)
        bidi_text = get_display(reshaped_text)
        
        start_time = i / sr
        end_time = (i + batch_size) / sr
        print(f"Transcription for batch {i // batch_size + 1} ({start_time:.2f}s - {end_time:.2f}s): {bidi_text}") 
