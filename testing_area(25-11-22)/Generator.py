''''
    this generator file contains all the generator classes for returning [Score(s), File Name, ...]
    
    - Scores contain : rate (speed), pitch, articulation, prounounciation, volume
    
    - File Name : contains the generated filename. Used for saving a file.
    
    - Feedback
'''

import uuid
import pytz
from datetime import datetime


class Score:

    def __word_count(self, text: list[str]) -> int:

        word_count: int = 0

        for words in text:
            words = words.split(' ')
            word_count += len(words)

        return word_count

    def grammar(self, input_text: list[str], correct_text: list[str]) -> float:
        # open for algorithms on checking a specific sentence is grammatically correct.

        # get total number of words generated saved from text
        word_count: int = self.__word_count(input_text)

        # variables
        mistake: int = 0
        score: float = 0

        for sentence_a, sentence_b in zip(input_text, correct_text):

            # split the sentences, so we can get no 'spaces'
            sentence_a = sentence_a.split(' ')
            sentence_b = sentence_b.split(' ')

            # estimate the mistakes
            mistake += len(set(sentence_a).difference(sentence_b))

        # score = 100% - (mistake over total count times 100)
        score = 100-(mistake/word_count*100)
        return score

    def __speed(self, res) -> str:

        ideal = {'min': 2.33, 'max': 2.67}

        if res > ideal['max']:
            return 'fast'

        if res < ideal['min']:
            return 'slow'

        return 'ideal'

    def rate(self, text: list[str], time: float) -> float:
        '''
        Rate 
            Words / Time 
            140  to 160 wpm [ideal]
            2.33 to 2.67 score 

            Note: Lower is Slower
                Higher is Faster

            Note: A voice record must be at at least 1 min duration to calculate this
        '''
        if time <= 0 or text[0] == '':
            return 0

        words: int = self.__word_count(text)
        result = words / time
        # for testing
        speed = self.__speed(result)

        result /= 2.67
        result *= 100
        result = result % 100 if result > 100 else result

        return result

    def __identify_hertz(self, gender, min, max) -> int:
        ...

    def __identify_gender(self, voice) -> str:
        # testing ..... voice must be identified before deciding the gender
        gender = 'male' if voice == '' else 'female'
        return gender

    def pitch(self, audio) -> float:
        '''
        Pitch: Male [85-180 hertz] & Female [165-255 hertz]
        Note: this can be seen in Spectrogram's 'Y-Axis'
        '''

        # test, suppose audio is none this time
        m_hertz: list = [85, 180]  # m_hertz[0], m_hertz[1]
        f_hertz: list = [165, 255]  # f_hertz[0], f_hertz[1]

        # identify the gender voice
        gender = self.__identify_gender(audio)

        score = 0

        hertz = self.__identify_hertz(gender, m_hertz[0], m_hertz[1]) if gender[0] == 'm' else self.__identify_hertz(
            gender, f_hertz[0], f_hertz[1])

        return score + hertz

    def articulation(self) -> None:
        '''
        Articulation
            Using MAR (Mean Articulatory Rate)
            10 - 20 consecutive syllables 

            Note: this is for fluent speech without pauses, MAR technique is a reliable approach for determining articulation rate.

            - dependent on words & voice
            - Using MAR (Mean Articulatory Rate)
        '''

    def prounounciation(self) -> None:
        '''
        Pronunciation
            Using Google Dictionary API

        - dependent on words & voice
        '''

    def volume(self) -> None:
        '''
        Volume
            Represented by Colours
            Low Volume  ⇒ Black to Red
            High Volume ⇒ Yellow to White

            Note: our group is still thinking if we are going to specify a specific speech distance when using the app

        dependent on voice & spectogram
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

    def for_wav(self) -> str:
        return f'{self.__file_name()}.wav'

    def for_txt(self) -> str:
        return f'{self.__file_name()}.txt'


class Feedback:

    # total need to return for feedback
    __TOTAL_NEEDED: int = 6

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
        total_score = 0
        for index in self.scores:
            total_score += self.scores[index]
        return total_score / self.__TOTAL_NEEDED

    def feedback(self) -> None:
        score = self.scores
        total_score = self.__get_total_avg_score()

        for index in self.scores:
            print(f'{score[index]}%\tfor {index} -> \tremarks: ', end='')
            print('good') if score[index] > 85 else print('bad')

        print(f'\noverall score feedback: {total_score} -> remarks: ', end='')
        print('good') if total_score > 85 else print('bad')

        # generate the words for feedback
