from Score_Generator import Score as check


def main():
    # suppose, it is already in (clean state)
    # suppose, a raw data example
    text_data: list = [
        'my name is Joemar',
        'and i lives in my houses',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # do grammar check, below is just an example
    correction: list = [
        'my name is Joemar',
        'and i live in my house',  # suppose 'live' and 'house'
        'i do a lot of chores',
    ]

    # get score(s)
    grammar_score = check.grammar(text_data, correction)

    # print score(s)
    print(f'grammar score: {grammar_score}')


if __name__ == "__main__":
    main()
