import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from time import sleep
import speech_recognition as sr
import whisper as wh
from transformers import *
import torch
import soundfile as sf
import os
import torchaudio


def whisper_model(filepath: Path) -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    model = wh.load_model("large")
    os.system('cls' if os.name == 'nt' else 'clear')
    return model.transcribe(str(filepath)).get("text")

def sphinx_model(filepath: Path) -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)
    os.system('cls' if os.name == 'nt' else 'clear')
    return r.recognize_sphinx(audio)

def wave2vec2_model(filepath: Path) -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    model_name = "facebook/wav2vec2-base-960h"
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    audio_url = str(filepath)
    speech, sr = torchaudio.load(audio_url)
    speech = speech.squeeze()
    resampler = torchaudio.transforms.Resample(sr, 16000)
    speech = resampler(speech)
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000)["input_values"]
    logits = model(input_values)["logits"]
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    os.system('cls' if os.name == 'nt' else 'clear')
    return transcription.lower()

def runner(filepath: Path) -> str:

    res = []

    with ThreadPoolExecutor(max_workers=3) as executor:

        whisper = executor.submit(whisper_model, filepath)
        sphinx = executor.submit(sphinx_model, filepath)
        wave2vec2 = executor.submit(wave2vec2_model, filepath)

        res = [whisper.result(), sphinx.result(), wave2vec2.result()]

    return res

