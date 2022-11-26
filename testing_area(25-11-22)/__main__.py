from Generator import Score, File_Name


def main():

    # instances
    check = Score()
    generated = File_Name()

    # ################################################################### #

    # suppose, it is already in (clean state)
    # suppose, a raw data example
    text: list[str] = [
        'my name is Joemar',
        'and i lives in my houses',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # do grammar check, below is just an example
    correct: list[str] = [
        'my name is Joemar',
        'and i live in my house',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # get file names [sample]
    # print(f'wav file name used: {generated.wav_file_name()}')
    # print(f'txt file name used: {generated.txt_file_name()}')

    # ################################################################### #

    # get score(s) [sample]
    grammar_score: float = check.grammar(text, correct)
    print(f'\ngrammar score: {grammar_score}%', end='')

    # get pitch
    # pitch_score: float = check.pitch('1')  # suppose audio
    # print(f'\npitch score: {pitch_score}%', end='')


if __name__ == "__main__":
    main()
