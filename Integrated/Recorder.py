__authors__ = "joemar_olan_glenn_arrlee_jericho"
__version__ = "1.5"
__docformat__ = "restructuredtext en"

try:

    import os
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


def _emptydir(directory: str):
    ''''
        used for chcking if directory exist or not
        - if not exist, then create one
        - else do nothing
    '''
    if not (directory and not directory.isspace()):
        return

    _path = ''
    for dir in directory.split('/'):
        _path += dir+'/'
        if os.path.isdir(_path) == False:
            os.mkdir(_path)


class Recorder:

    def get_txt_file_name(self) -> str:
        '''
            get txt file generated name
        '''
        return self.file_name + '.txt'

    def get_wav_file_name(self) -> str:
        '''
            get wav file generated name
        '''
        return self.file_name + '.wav'

    def get_audio_duration(self, audio_path):
        # read audio and get framerate and number of frames
        audio = wave.open(audio_path, 'rb')
        frate = audio.getframerate()
        nframe = audio.getnframes()
        # get time of the audio in seconds
        t_audio_in_sec = nframe / frate
        # val = wave_form.getnframes()
        audio.close()
        return t_audio_in_sec

    def save(self, audio, frames) -> None:
        '''
            save audio file by getting the audio and the frames
            - audio save
            - text save
        '''
        try:
            # saving path
            PATH: str = 'audio/dataset/'
            _emptydir(PATH)

            # config, get generated file name with no extention
            file = File().generated_name()

            # put it in a self variable to be accessed by other functions
            self.file_name = PATH + file

            # file now is a wav file
            file = PATH + file + '.wav'

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
                file,
                fp16=False,
                language='English',
                task='Translate'
            )

            text = str(result["text"])
            text = str(text).split('.')

            # get the txt (transcribed text) from that audio
            file = self.get_txt_file_name()

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
        record_time: int = _MIN * _SEC

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
