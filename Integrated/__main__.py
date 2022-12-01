
try:
    import os
    from Generator import Score, File
    from Recorder import Recorder
except Exception:
    print('import error occur')
    raise


def main():
    # object instances
    check = Score()
    generated = File()
    recorder = Recorder()

    # ################################################################### #

    print("start rec...")
    # record_file = recorder.record()
    print("rec stop...")

    # record[0] -> contains the audio & record[1] -> constains the frames
    # recorder.save(record_file['audio'], record_file['frames'])

    # ################################################################### #

    # get audio file, text generated file
    _tempf = txt_file = 'audio/dataset/2211306d9b7338-705f-11ed-80dc-708bcd015b0c3318.txt'

    # ################################################################### #

    # get score(s) [sample]
    grammar_score: float = check.grammar(txt_file)
    speed_score: float = check.rate(txt_file, 5)
    # CREATE A FUNCTION IN RECORD TO RETURN THE SPEED, for input in this speed ELSE put inside the function rate (the task to get the speed)

    # gender identified test
    wav_file = str(_tempf)[:-3] + 'wav'
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
    check.total_average_feedback()


if __name__ == "__main__":
    main()
