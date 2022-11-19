'''
    requires math plot lib numpy --> pip install matplotlib numpy

    this program is to plot the audio for visualization
'''

import wave
import matplotlib.pyplot as plt
import numpy as np

# open (read binary)
audio = wave.open('/workspaces/SE1_Project//audio/sample_mar1.wav', 'rb')

sample_freq = audio.getframerate()
n_samples = audio.getnframes()
signal_wave = audio.readframes(-1)

# close
audio.close()

# get sec
t_audio = n_samples / sample_freq
print(t_audio)

# we need to create the plot by using the bytes object -> signal_wave
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
# start,end(len of the signal),number param
times = np.linspace(0, t_audio, num=n_samples)
# plotting
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time in sec")
plt.xlim(0, t_audio)
plt.show()
