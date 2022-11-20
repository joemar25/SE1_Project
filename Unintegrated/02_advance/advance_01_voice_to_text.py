'''
- if we are going to use an api, we need to import 2 things: API link, and Request
- for now, we will use speech recognition by installing : pip install SpeechRecognition
    Speech recognition engine/API support:
        CMU Sphinx (works offline)
        Google Speech Recognition
        Google Cloud Speech API
        Wit.ai
        Microsoft Bing Voice Recognition
        Houndify API
        IBM Speech to Text
        Snowboy Hotword Detection (works offline)

    Quickstart: pip install SpeechRecognition. See the “Installing” section for more details.
                To quickly try it out, run python -m speech_recognition after installing.

    !important: Together with pyaudio, we can record something from our mic
'''

import pyaudio
import speech_recognition as sr


# main function
def main():
    # who will listin? -listerer
    listener = sr.Recognizer()

    # recording audio might return an error (hint: use try catch)
    try:

        # use microphone, so that the listener can listen to it
        with sr.Microphone() as source:

            print("start recording...")
            voice = listener.listen(source)

            # once souce is completely recognize, we can use a function(s)
            # in which is souce can be converted (ex. speech to text)

            # passing audio to google then return it as string
            speech = listener.recognize_google(voice)

            # test
            print(speech)
            print("end recording...")

    except Exception:
        pass


main()
