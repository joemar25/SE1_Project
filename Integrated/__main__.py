
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
    record_file = recorder.record()
    print("rec stop...")

    # record[0] -> contains the audio & record[1] -> constains the frames
    recorder.save(record_file['audio'], record_file['frames'])

    # ################################################################### #

    # get audio file, text generated file
    _tempf = file = recorder.get_txt_file_name()

    print(file)
    # open text file and read it and save to text
    with open(file, 'r') as file:
        text: list[str] = file.readlines()

    # # remove \n
    text = [i.strip() for i in text]

    # # do grammar check, below is just an example
    correct: list[str] = [
        'my name is Joemar',
        'and i live in my house',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # ################################################################### #

    # get score(s) [sample]
    grammar_score: float = check.grammar(text, correct)
    speed_score: float = check.rate(text, 5)

    # gender identified test
    wav_file = str(_tempf)[:-3] + 'wav'
    gender: str = check.test_identify_gender(wav_file)

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
    print('gender of the speaker is:', gender)
    check.total_average_feedback()


if __name__ == "__main__":
    main()
