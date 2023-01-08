import whisper as wh 
model = wh.load_model("large-v2" )

result = model.transcribe('machine-learning_speech-recognition_16-122828-0002.wav')

print(result)