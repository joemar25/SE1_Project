''''
    this generator file contains all the generator classes for returning [Score(s), File Name, ...]
    
    - Scores contain : rate (speed), pitch, articulation, prounounciation, volume
    
    - File Name : contains the generated filename. Used for saving a file.
'''

import uuid
import pytz
from datetime import datetime


class Score:

    def grammar(self, input_text: list[str], correct_text: list[str]) -> float:
        '''
        Grammar
            Using Grammarly API
        '''

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
    def rate(self):
        '''
        Rate 
            Words / Time 
            140  to 160 wpm [ideal]
            2.33 to 2.67 score 

            Note: Lower is Slower
                Higher is Faster
        '''

    def pitch(self):
        '''
        Pitch
            Male [85-180 hertz]
            Female [165-255 hertz]

            Note: this can be seen in Spectrogram's 'Y-Axis'
        '''

    def articulation(self):
        '''
        Articulation
            Using MAR (Mean Articulatory Rate)
            10 - 20 consecutive syllables 

            Note: this is for fluent speech without pauses, MAR technique is a reliable approach for determining articulation rate.
        '''

    def prounounciation(self):
        '''
        Pronunciation
            Using Google Dictionary API
        '''

    def volume(self):
        '''
        Volume
            Represented by Colours
            Low Volume  ⇒ Black to Red
            High Volume ⇒ Yellow to White

            Note: our group is still thinking if we are going to specify a specific speech distance when using the app
        '''


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

    def __get_total_avg_score(self) -> float:
        generated_total = 0
        for index in self.scores:
            generated_total += self.scores[index]
        return generated_total / self.TOTAL

    def feedback(self):
        score = self.scores
        total_score = self.__get_total_avg_score()

        for index in self.scores:
            print(f'{score[index]}%\tfor {index} -> \tremarks: ', end='')
            print('good') if score[index] > 85 else print('bad')

        print('\noverall score feedback: ', end='')
        print('good') if total_score > 85 else print('bad')

        # generate the words for feedback
