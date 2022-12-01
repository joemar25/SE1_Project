
from gingerit.gingerit import GingerIt
from Generator import Score

score = Score()
# get audio file, text generated file
txt_file = 'audio/dataset/2211306d9b7338-705f-11ed-80dc-708bcd015b0c3318.txt'
print(score.grammar(txt_file))
