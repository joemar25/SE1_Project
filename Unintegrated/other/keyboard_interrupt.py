import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2
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

seconds = 30
frames = []
try:
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)  # read 3200 per iteration
        frames.append(data)
except KeyboardInterrupt:
    ...

print("recording end...")

stream.stop_stream()
stream.close()
audio.terminate()

file = './audio/sample_mar1_out_keyboard_in.wav'
wave_form = wave.open(file, 'wb')
wave_form.setnchannels(CHANNELS)
wave_form.setsampwidth(audio.get_sample_size(FORMAT))
wave_form.setframerate(RATE)
wave_form.writeframes(b''.join(frames))
wave_form.close()
