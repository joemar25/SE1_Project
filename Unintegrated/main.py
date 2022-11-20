# necessary imports for generating filename and manipulating audio file
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

print("start recording...")
frames = []
minutes = 1
seconds = 5
record_time = minutes * seconds

# loop till frames len is same as (rate/fpb*rec_time)
for i in range(0, int(RATE / FRAMES_PER_BUFFER * record_time)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
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
