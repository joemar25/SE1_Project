from Generator import Score, File, Feedback


def main():

    # instances
    check = Score()
    generated = File()

    # ################################################################### #

    # suppose, it is already in (clean state)
    # suppose, a raw data example
    # file list will contain the files from dataset folder
    file_list = generated.files_from_dataset('txt')

    # open text file and read it and save to text
    with open(file_list[0], 'r') as file:
        text = file.readlines()

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
    print(f'\ngrammar score: {grammar_score}%', end='')

    # get pitch
    # pitch_score: float = check.pitch('1')  # suppose audio
    # print(f'\npitch score: {pitch_score}%', end='')


if __name__ == "__main__":
    main()
