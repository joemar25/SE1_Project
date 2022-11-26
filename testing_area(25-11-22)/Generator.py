import uuid
import pytz
from datetime import datetime


class Score:

    '''
        this is just a test...
    '''

    def grammar(self, input_text: list[str], correct_text: list[str]):

        # variables
        word_count: int = 0
        mistake: int = 0
        score: float = 0

        for sentence_a, sentence_b in zip(input_text, correct_text):

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


# File_Name_Generator Class
class File_Name:

    def file_name(self):
        # uses: uuid, pytz, datetime
        todays: datetime = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
        utime: str = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

        deduct :int= -2 if str(todays.year)[1] == '0' else -3
        udate :str= f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"

        return f"{udate}{utime}"

    def wav_file_name(self):
        return f'{self.file_name()}.wav'
