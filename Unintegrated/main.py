# necessary imports for generating filename and manipulating audio file
import whisper
from datetime import datetime
import pytz
import uuid
import pyaudio
import wave


# Constants
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
EXTENTION = '.wav'


# function to generate filename
def filename_generator():
    todays = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
    utime = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

    deduct = -2 if str(todays.year)[1] == '0' else -3
    udate = f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"
    return f"{udate}{utime}"


# main
audio = pyaudio.PyAudio()
stream = audio.open(
    frames_per_buffer=FRAMES_PER_BUFFER,
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True
)

frames = []
minutes = 5
seconds = 60
record_time = minutes * seconds  # this records for 5 min

print("start recording...")
try:
    # loop till frames len is same as (rate/fpb*rec_time)
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * record_time)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

except KeyboardInterrupt:
    ...
print("recording end...")

# close steam and audio
stream.stop_stream()
stream.close()
audio.terminate()

# config
FILE = './audio/dataset/'+filename_generator()+EXTENTION
SAMPWIDTH = audio.get_sample_size(FORMAT)
FRAMES = b''.join(frames)

# save
wave_form = wave.open(FILE, 'wb')
wave_form.setnchannels(CHANNELS)
wave_form.setsampwidth(SAMPWIDTH)
wave_form.setframerate(RATE)
wave_form.writeframes(FRAMES)
wave_form.close()

################################################
model = whisper.load_model('tiny')

result = model.transcribe(
    FILE,
    fp16=False,
    language='English',
    task='Translate'
)

text = str(result["text"])
text = " ".join(text.split())
text = str(text).split('.')

print(text)
