from Generator import Score, File_Name


def main():

    # instances
    check = Score()
    name = File_Name()

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

    # ################################################################### #

    # get file name for the wav
    name = name.wav_file_name()

    print(f'file name: {name}')

    # ################################################################### #

    # get score(s)
    grammar_score: float = check.grammar(text, correct)

    print(f'grammar score: {grammar_score}%')


if __name__ == "__main__":
    main()
