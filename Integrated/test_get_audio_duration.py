from Recorder import Recorder

path = 'audio/female.wav'
rec = Recorder()
a = rec.get_audio_duration(path)
print(a)
