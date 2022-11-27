from Generator import Score, File


def main():

    # object instances
    check = Score()
    generated = File()

    # ################################################################### #

    # suppose, it is already in (clean state)
    # suppose, a raw data example
    # file list will contain the files from dataset folder
    file_list = generated.files_from_dataset('txt')

    # open text file and read it and save to text
    with open(file_list[0], 'r') as file:
        text: list[str] = file.readlines()

    # remove \n
    text = [i.strip() for i in text]

    # do grammar check, below is just an example
    correct: list[str] = [
        'my name is Joemar',
        'and i live in my house',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # get file names [sample]
    print(f'txt file name used: {file_list[0]}')

    # ################################################################### #

    # get score(s) [sample]
    grammar_score: float = check.grammar(text, correct)
    speed_score: float = check.rate(text, 5)

    # printing values
    print('\nscores')
    print(f'rate: {speed_score}%')
    print(f'grammar: {grammar_score}%')

    # ################################################################### #
    # result = Feedback(grammar_score, speed_score, 80, 80, 80, 80)

    # on rate, it is mandated to have the time of the audio file
    print('rate feedback: '+check.feedback_for('rate'))
    print('total average:', check.get_total_average())


if __name__ == "__main__":
    main()
