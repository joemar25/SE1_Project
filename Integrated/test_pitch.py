from Generator import Score

score = Score()

path = 'audio/sample_mar1.wav'

r = score.pitch(path)

print(r)