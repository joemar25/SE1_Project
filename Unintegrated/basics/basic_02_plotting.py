# requires math plot lib numpy --> pip install matplotlib numpy

import wave
import matplotlib.pyplot as plt
import numpy as np

# open (read binary)
audio = wave.open('/workspaces/SE1_Project//audio/sample_mar1.wav', 'rb')

channels = audio.getnchannels()
sfreq = audio.getframerate()
nsample = audio.getnframes()
signal_wave = audio.readframes(-1)

# close
audio.close()

# get sec
t_audio = nsample / sfreq
# test -> print(t_audio)


# we need to create the plot by using the bytes object -> signal_wave
