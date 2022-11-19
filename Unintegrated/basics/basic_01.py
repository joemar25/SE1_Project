'''
    @audio file formats
        example: .mp3, .flac, .wav, .ogg, etc.

        dictionary: 'compress' is a process

        mp3 - most popular, but a lossy compression format
              means that it compresses
              the data that it can lose information
        flac - also popular, but a loss lesscompression format
              means that it compresses
              the data but allows us to perfectly reconstruct
              the original data
        wav - (stands for: wave form audio format)
              is a uncompressed format
              means that it stores data in a uncompressed way.
              the audio quality here is the best but the
              file size is the largest

        note: we will use wav since it is easier to work with in python

              importing wave requires no installation (it is pre-build)

        before loading some data in a wave file, we need to understand some parameters
        (audio signal param)

        dictionary: 'channel' is direction

        - number of channels
            - usually 1 (mono) or 2 (stereo)
                  number of the independent channels
                  example: stereo - has 2 independent channels
                                    which gives us the expression that
                                    the audio is coming from 2 different directions

        - sample width
            - the number of bytes for each sample

        - framerate/sample_rate
            - knowns as sample_rate or sample_frequency
            - most important parameters
                  example: 44100hz, is the standard sample rate for CD quality
                              means we get 44100hz sample value per seconds

        - number of frames
            - the total number of frames

        - values of a frame
            - when loaded, this would be in binary format (but convertable to int)
'''

import wave

# read binary
audio = wave.open('/workspaces/SE1_Project//audio/sample_mar1.wav', 'rb')

# set in variables
channels = audio.getnchannels()
swidth = audio.getsampwidth()
frate = audio.getframerate()
nframe = audio.getnframes()
params = audio.getparams()

# printing the basics
print(f'channels  : {channels}')  # get number of channels
print(f'width     : {swidth}')  # get number of width
print(f'frame rate: {frate}')  # get number of frame rate
print(f'num frames: {nframe}')  # get number of frames
print(f'parameters: {params}')  # get all paremeters in the audio

# get time of the audio in seconds
t_audio_in_sec = nframe / frate
print(f'\naudio time in secs: {t_audio_in_sec}')

# get actual frames
frames = audio.readframes(-1)
print(f'frames object       : {type(frames)}')  # class is bytes
print(f'frame first byte    : {type(frames[0])}')  # extract 1st bytes

print(f'frames length       : {len(frames)}')

# len(frame) --> not same as the number of frames (nframes) since it is twice as much
# swidth is 2 right
# so, to get the nframe of the readed frame is to divide it the by swidth (basically 2)
# but dividing 2 to the frames length is not enough

# take note that swidth is 2... so i have made some experement...
# note: i haved observe that if channel is 2 (sterio), then it must be multiplied so -> (2*2)
#       so inconclusion, we need to multiply channel and width and divide it to the frame length
#       to get the same value as nframe

divisor = channels*swidth
print(f'frames length / {divisor}   : {len(frames)/divisor}')

# we are done with the basics of reading a simple .wav file

# ------------------------------------------------------------------

# to save data again

# write binary
new_audio = wave.open(
    '/workspaces/SE1_Project//audio/sample_mar1_duplicate.wav', 'wb')

# basically we need to change the getters from above to setters
new_audio.setnchannels(channels)
new_audio.setsampwidth(swidth)
new_audio.setframerate(frate)

# write n frame
new_audio.writeframes(frames)

# close
new_audio.close()
audio.close()
