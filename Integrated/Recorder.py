__author__ = "Joemar25"
__version__ = "1.5"
__docformat__ = "restructuredtext en"


import os

try:

    import whisper
    import wave
    import _portaudio as pa

    from pyaudio import PyAudio as py_audio
    from Generator import File

except ImportError as e:
    print(e)
    raise

# recording limit
_SEC: int = 60
_MIN: int = 5

# audio format
_FRAMES_PER_BUFFER: int = 3200
_CHANNELS: int = 2
_RATE: int = 48000
_FORMAT = pa.paInt16

''''
    used for chcking if directory exist or not
        - if not exist, then create one
        - else do nothing
'''


def _emptydir(directory: str):
    if not (directory and not directory.isspace()):
        return

    _path = ''
    for dir in directory.split('/'):
        _path += dir+'/'
        if os.path.isdir(_path) == False:
            os.mkdir(_path)


class Recorder:

    def save(self, audio, frames) -> None:
        ####################### AUDIO SAVE #######################

        try:
            # saving path
            PATH: str = 'audio/dataset/'
            _emptydir(PATH)

            # # config
            wav_file = File().wav_generated_name()
            file = PATH + wav_file
            SAMPWIDTH = audio.get_sample_size(_FORMAT)
            FRAMES = b''.join(frames)

            # save
            wave_form = wave.open(file, 'wb')
            wave_form.setnchannels(_CHANNELS)
            wave_form.setsampwidth(SAMPWIDTH)
            wave_form.setframerate(_RATE)
            wave_form.writeframes(FRAMES)
            wave_form.close()

        ######################## TXT SAVE ########################

            model = whisper.load_model('tiny')
            result = model.transcribe(
                file, # ERROR 
                fp16=False,
                language='English',
                task='Translate'
            )

            text = str(result["text"])
            text = str(text).split('.')

            file = audio[:-4]+'.txt'

            # save
            with open(file, 'w') as f:
                for line in text:
                    if line != '':
                        line = ' '.join(line.split())
                        f.write(line+'\n')

            # terminate audio
            audio.terminate()

        except Exception as e:
            print(e)

    def record(self) -> dict:

        audio = py_audio()

        stream = audio.open(
            frames_per_buffer=_FRAMES_PER_BUFFER,
            channels=_CHANNELS,
            format=_FORMAT,
            rate=_RATE,
            input=True
        )

        frames: list = []
        record_time = _MIN * _SEC

        try:

            for _ in range(0, int(_RATE / _FRAMES_PER_BUFFER * record_time)):
                data = stream.read(_FRAMES_PER_BUFFER)
                frames.append(data)

        except KeyboardInterrupt:
            ...

        # close
        stream.stop_stream()
        stream.close()

        # save
        return {'audio': audio, 'frames': frames}


# test
recorder = Recorder()

# record audio
print("start recording...")
record_file = recorder.record()
print("record stop...")

# record[0] -> contains the audio & record[1] -> constains the frames
recorder.save(record_file['audio'], record_file['frames'])
