# import speech_recognition as sr
from speech_recognition import Recognizer, AudioFile


# main function
def main():
    # who will listen? - listerer
    listener = Recognizer()

    # recording audio might return an error (hint: use try catch)
    try:
        # file = sr.AudioFile('./audio/sample_mar1.wav')  # the source
        # the source
        file = AudioFile(
            './audio/dataset/221120822e0e1c-687d-11ed-9470-708bcd015b0c24618.wav')
        with file as source:  # use the file source

            # noice handling
            listener.adjust_for_ambient_noise(source)

            # listining to the souce
            voice = listener.listen(source)

            # passing audio to google (or diff api) then return it as string
            text = listener.recognize_google(voice)
            # text = text.lower() # this makes the generated text lower

            # test
            print(text)

    except Exception as e:
        print(f"Error message says... {e}")


# check is code is being run
if __name__ == "__main__":
    main()

    # _ = means don't use me
