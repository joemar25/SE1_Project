import whisper
from datetime import datetime
import pytz
import uuid
import pyaudio
import wave

# recording limit
SEC: int = 60
MIN: int = 5

# audio format
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
EXTENTION = '.wav'


def filename_generator():
    todays = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
    utime = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

    deduct = -2 if str(todays.year)[1] == '0' else -3
    udate = f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"
    return f"{udate}{utime}"


def save_text(audio):
    model = whisper.load_model('tiny')

    result = model.transcribe(
        audio,
        fp16=False,
        language='English',
        task='Translate'
    )

    text = str(result["text"])
    text = str(text).split('.')

    file = audio[:-4]+'.txt'

    with open(file, 'w') as f:
        for line in text:
            if line != '':
                line = ' '.join(line.split())
                f.write(line+'\n')


def save_audio(audio, frames):
    file = './audio/dataset/'+filename_generator()+EXTENTION
    SAMPWIDTH = audio.get_sample_size(FORMAT)
    FRAMES = b''.join(frames)

    # save
    wave_form = wave.open(file, 'wb')
    wave_form.setnchannels(CHANNELS)
    wave_form.setsampwidth(SAMPWIDTH)
    wave_form.setframerate(RATE)
    wave_form.writeframes(FRAMES)
    wave_form.close()

    # to_text
    save_text(file)


def record():
    audio = pyaudio.PyAudio()
    stream = audio.open(
        frames_per_buffer=FRAMES_PER_BUFFER,
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True
    )

    frames = []
    record_time = MIN * SEC

    print("start recording...")
    try:

        for i in range(0, int(RATE / FRAMES_PER_BUFFER * record_time)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)

    except KeyboardInterrupt:
        ...
    print("recording end...")

    # close
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save
    save_audio(audio, frames)
