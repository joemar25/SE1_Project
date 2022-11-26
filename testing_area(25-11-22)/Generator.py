''''
    this generator file contains all the generator classes for returning [Score(s), File Name, ...]
    
    - Scores contain, how user's grammar is accurately correct
                      .......... rate (speed)
                      .......... pitch
                      .......... articulation
                      .......... prounounciation
                      .......... volume
    
    - File Name, contains the generated filename. Used for saving a file.
'''

import uuid
import pytz
from datetime import datetime


class Score:

    '''
        this is just a test...
    '''

    def grammar(self, input_text: list[str], correct_text: list[str]) -> float:

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

    # speed
    def rate(self, input_text: list[str], correct_text: list[str]):
        ...

    def pitch(self, input_text: list[str], correct_text: list[str]):
        ...

    def articulation(self, input_text: list[str], correct_text: list[str]):
        ...

    def prounounciation(self, input_text: list[str], correct_text: list[str]):
        ...

    def volume(self, input_text: list[str], correct_text: list[str]):
        ...


# File_Name_Generator Class
class File_Name:

    def __file_name(self) -> str:
        # uses: uuid, pytz, datetime
        todays: datetime = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
        utime: str = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

        deduct: int = -2 if str(todays.year)[1] == '0' else -3
        udate: str = f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"

        return f"{udate}{utime}"

    def wav_file_name(self) -> str:
        return f'{self.__file_name()}.wav'

    def txt_file_name(self) -> str:
        return f'{self.__file_name()}.txt'


class Feedback:

    TOTAL: int = 6

    def __init__(self, grammar_score: float, rate_score: float, pitch_score: float, articulation_score: float, prounounciation_score: float, volume_score: float) -> None:
        self.scores = {
            'grammar': grammar_score,
            'rate': rate_score,
            'pitch': pitch_score,
            'articulation': articulation_score,
            'prounounciation': prounounciation_score,
            'volume': volume_score,
        }

    def __get_total_score(self) -> float:
        generated_total = 0
        for i in self.scores:
            generated_total += self.scores[i]
        return generated_total / self.TOTAL

    def feedback(self):
        score = self.scores
        total_score = self.__get_total_score()

        for i in self.scores:
            print(f'{i}: ', end='')
            print('good') if score[i] > 85 else print('bad')

        print('overall score feedback: ', end='')
        print('good') if total_score > 85 else print('bad')
