from Generator import Score
import os

score = Score()

path = 'audio/female.wav'

r = score.pitch(path)

os.system('cls')
print(score.test_identify_gender(path))
