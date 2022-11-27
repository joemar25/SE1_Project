from Generator import File_Name
import whisper
import pytz
import uuid
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

        path = ''
        for dir in directory.split('/'):
            path += dir+'/'
            if os.path.isdir(path) == False:
                os.mkdir(path)

    def __save_audio(self, audio, frames) -> None:

        PATH: str = 'audio/dataset'
        # directory cheker if exit
        self.__emptydir(PATH)

        wav_file = File_Name().wav_file_name()
        file = './audio/dataset/' + wav_file
        SAMPWIDTH = audio.get_sample_size(self.__FORMAT)
        FRAMES = b''.join(frames)

        # save
        wave_form = wave.open(file, 'wb')
        wave_form.setnchannels(self.__CHANNELS)
        wave_form.setsampwidth(SAMPWIDTH)
        wave_form.setframerate(self.__RATE)
        wave_form.writeframes(FRAMES)
        wave_form.close()

        # to_text
        # save_text(file)

    def record(self):
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
        self.__save_audio(audio, frames)
