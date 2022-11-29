'''
    @tam17aki tam17aki/inaSpeechSegmenter_demo.py
    ref: https://gist.github.com/tam17aki/11eb1566a2d48b382607d23dddb98891
    lang = Japanese
    
    has fun installation process...
'''


from inaSpeechSegmenter import Segmenter
from pydub import AudioSegment

input_file = 'audio/sample_mar1.wav'

output_file = 'audio/segment'

seg = Segmenter(vad_engine='smn', detect_gender=False)

segmentation = seg(input_file)

speech_segment_index = 0
for segment in segmentation:
    segment_label = segment[0]

    if (segment_label == 'speech'):

        start_time = segment[1] * 1000
        end_time = segment[2] * 1000

        newAudio = AudioSegment.from_wav(input_file)
        newAudio = newAudio[start_time:end_time]
        output_file = output_file + str(speech_segment_index) + '.wav'
        newAudio.export(output_file, format="wav")

        speech_segment_index += 1
        del newAudio
