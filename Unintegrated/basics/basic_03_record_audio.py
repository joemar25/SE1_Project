'''
record audio using pyaudio (also play audio)
which is installed using, python -m pip install pyaudio (on windows)
'''
import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2  # mono(1) is for test but sterio (2) is beeter
RATE = 48000

audio = pyaudio.PyAudio()
stream = audio.open(
    frames_per_buffer=FRAMES_PER_BUFFER,
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True
)

print("start recording...")

seconds = 5
frames = []

for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)  # read 3200 per iteration
    frames.append(data)

print("recording end...")

stream.stop_stream()
stream.close()
audio.terminate()

file = './audio/sample_mar1_out.wav'
wave_form = wave.open(file, 'wb')
wave_form.setnchannels(CHANNELS)
wave_form.setsampwidth(audio.get_sample_size(FORMAT))
wave_form.setframerate(RATE)
wave_form.writeframes(b''.join(frames))
wave_form.close()
