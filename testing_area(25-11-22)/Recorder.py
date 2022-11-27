from Generator import File
import whisper
import pyaudio
import wave
import os


class Recorder:

    # recording limit
    __SEC: int = 60
    __MIN: int = 5

    # audio format
    __FRAMES_PER_BUFFER = 3200
    __FORMAT = pyaudio.paInt16
    __CHANNELS = 2
    __RATE = 48000

    def __emptydir(self, directory):
        # make a directory if it doesn't exist

        if(not (directory and not directory.isspace())):
            return

        _path = ''
        for dir in directory.split('/'):
            _path += dir+'/'
            if os.path.isdir(_path) == False:
                os.mkdir(_path)

    def __save_text(self, audio) -> None:
        model = whisper.load_model('tiny')

        # result = model.transcribe(
        #     audio,
        #     fp16=False,
        #     language='English',
        #     task='Translate'
        # )

        # text = str(result["text"])
        # text = str(text).split('.')

        # file = audio[:-4]+'.txt'

        # # save
        # with open(file, 'w') as f:
        #     for line in text:
        #         if line != '':
        #             line = ' '.join(line.split())
        #             f.write(line+'\n')

    def __save_audio(self, audio, frames) -> None:

        PATH: str = 'audio/dataset/'
        # directory cheker if exit
        self.__emptydir(PATH)

        wav_file = File().wav_generated_name()
        file = PATH + wav_file
        SAMPWIDTH = audio.get_sample_size(self.__FORMAT)
        FRAMES = b''.join(frames)

        # save
        wave_form = wave.open(file, 'wb')
        wave_form.setnchannels(self.__CHANNELS)
        wave_form.setsampwidth(SAMPWIDTH)
        wave_form.setframerate(self.__RATE)
        wave_form.writeframes(FRAMES)
        wave_form.close()

    def save(self, audio, frames) -> None:
        self.__save_text(audio)
        self.__save_audio(audio, frames)

    def record(self) -> dict:
        audio = pyaudio.PyAudio()
        stream = audio.open(
            frames_per_buffer=self.__FRAMES_PER_BUFFER,
            format=self.__FORMAT,
            channels=self.__CHANNELS,
            rate=self.__RATE,
            input=True
        )

        frames = []
        record_time = self.__MIN * self.__SEC

        try:

            for i in range(0, int(self.__RATE / self.__FRAMES_PER_BUFFER * record_time)):
                data = stream.read(self.__FRAMES_PER_BUFFER)
                frames.append(data)

        except KeyboardInterrupt:
            ...

        # close
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # save
        return {'audio': audio, 'frames': frames}
