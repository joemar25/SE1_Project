class Score:

    '''
        this is just a test...
    '''

    def grammar(self, text_data: list[str], correction: list[str]): 

        # variables
        word_count: int = 0
        mistake: int = 0
        score: float = 0

        for sentence_a, sentence_b in zip(text_data, correction):

            # split the sentences, so we can get no 'spaces'
            sentence_a = sentence_a.split(' ')
            sentence_b = sentence_b.split(' ')

            # get total words
            if len(sentence_a) > len(sentence_b):
                word_count += len(sentence_a)
            else:
                word_count += len(sentence_b)

            # estimate the mistakes
            mistake += len(set(sentence_a).difference(sentence_b))

        # score = 100% - (mistake over total count times 100)
        score = 100-(mistake/word_count*100)
        return score
