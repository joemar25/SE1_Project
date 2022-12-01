import whisper
model = whisper.load_model('medium')
# model = whisper.load_model('base')
audio_source = './audio/female.wav'
# result = model.transcribe(audio_source, fp16=False)
result = model.transcribe(
    audio_source,
    fp16=False,
    language='English', 
    task='Translate'
)
print(result["text"])
