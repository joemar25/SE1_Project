'''
    @tam17aki tam17aki/inaSpeechSegmenter_demo.py
    ref: https://gist.github.com/tam17aki/11eb1566a2d48b382607d23dddb98891
    lang = Japanese
    
    improvised by Joemar
    
    bug fixed...
    cpu support https://stackoverflow.com/questions/66092421/how-to-rebuild-tensorflow-with-the-compiler-flags
'''
from inaSpeechSegmenter import Segmenter

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


input_file = 'female_.wav'

seg = Segmenter(vad_engine='sm')

# by default gender dection is true, else set it to detect_gender=False
segmentation = seg(input_file)
gender = ['male', 'female']

# print(segmentation[0][0])

for s in segmentation:
    if gender[0] == s[0]:
        print(s[0])
        break
    if gender[1] == s[0]:
        print(s[0])
        break
