import whisper
model = whisper.load_model('medium')

audio_source = './audio/dataset/22112393cd8fdb-6b20-11ed-95e3-708bcd015b0c111838.wav'

result = model.transcribe(
    audio_source, 
    fp16=False,
language='English', 
task='Translate'
)

# remove additional space from string
text = str(result["text"])
text = " ".join(text.split())
text = str(text).split('.')

print(text)
