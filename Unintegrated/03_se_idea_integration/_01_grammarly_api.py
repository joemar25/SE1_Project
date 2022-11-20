# from speech_recognition import Recognizer, AudioFile
# from gingerit.gingerit import GingerIt


# # main function
# def main():
#     listener = Recognizer()
#     parser = GingerIt()
#     try:
#         # the source
#         file = AudioFile(
#             './audio/dataset/2211209e298bd8-68da-11ed-80f9-708bcd015b0c135248.wav')
#         with file as source:

#             listener.adjust_for_ambient_noise(source)
#             voice = listener.listen(source)
#             text = listener.recognize_google(voice, show_all=True)

#             aa = 'data is n go d'
#             # ct = parser.parse(aa)

#             # test
#             print("text is...", text)
#             # print("correct...", ct)

#     except Exception as e:
#         print(f"Error message says... {e}")


# if __name__ == "__main__":
#     main()
