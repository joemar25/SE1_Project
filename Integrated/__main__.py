__authors__ = "joemar_olan_glenn_arrlee_jericho"
__version__ = "1.5"
__docformat__ = "restructuredtext en"

try:

    import os
    from Generator import Score
    from Recorder import Recorder

except ImportError as e:
    print(e)
    raise


def main():
    # object instances
    check = Score()
    recorder = Recorder()

    # ################################################################### #

    print("start rec...")
    record_file = recorder.record()
    print("rec stop...")

    # save recording
    recorder.save(record_file['audio'], record_file['frames'])

    # ################################################################### #

    # get audio data
    txt_file: str = recorder.get_txt_file_name()
    wav_file: str = recorder.get_wav_file_name()
    audio_duration: float = recorder.get_audio_duration(wav_file)

    # ################################################################### #

    # get score(s) [sample]
    grammar_score: float = check.grammar(txt_file)
    speed_score: float = check.rate(txt_file, audio_duration)
    # CREATE A FUNCTION IN RECORD TO RETURN THE SPEED, for input in this speed ELSE put inside the function rate (the task to get the speed)

    # gender identified test
    # gender: str = check.test_identify_gender(wav_file)

    # clear scr
    os.system('cls')

    # printing values
    print('\nscores')
    print(f'rate: {speed_score}')
    print(f'grammar: {grammar_score}')

    # ################################################################### #
    # on rate, it is mandated to have the time of the audio file
    print('rate feedback:', check.feedback_for('rate'), '\n')
    print('total average:', check.get_total_average())
    # print('gender of the speaker is:', gender)
    # check.total_average_feedback()


if __name__ == "__main__":
    main()
