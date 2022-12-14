''''
    this generator file contains all the generator classes for returning [Score(s), File, ...]

    - Score: contains rate (speed), pitch, articulation, prounounciation, volume
        which includes Feedback, depending on the generated scores

    - File : contains the generated filename. Used for saving a file.
'''

__authors__ = "joemar_olan_glenn_arrlee_jericho"
__version__ = "1.5"
__docformat__ = "restructuredtext en"

try:
    import os
    import uuid
    import pytz
    from datetime import datetime
    from inaSpeechSegmenter import Segmenter
    from gingerit.gingerit import GingerIt
except ImportError as e:
    print(e)
    raise

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Score:

    # private variables for scores (used for total)
    __grammar_score: float = 0
    __rate_score: float = 0
    __pitch_score: float = 0
    __articulation_score: float = 0
    __volume_score: float = 0
    __prounounciation_score: float = 0

    # @todo: remove all score inside all funcition and make it global

    def __word_count(self, text: list[str]) -> int:
        '''
            returns word count of a specific list of text
        '''
        word_count: int = 0
        for words in text:
            words = words.split(' ')
            word_count += len(words)
        return word_count

    def grammar(self, input_text_dir: str) -> float:
        '''
            using gingerit module\n
            - will help us to catch gramatical errors and has the ability to correct it
        '''
        # gingerit object
        parser = GingerIt()

        # variables
        mistake: int = 0
        score: float = 0

        # open text file and read it and save to text
        with open(input_text_dir, 'r') as file:
            text: list[str] = file.readlines()

        # cleaning by removing '\n'
        text = [i.strip() for i in text]

        # get total number of words generated saved from text
        word_count: int = self.__word_count(text)

        if word_count != 0:
            # mistake counter
            for sentence in text:
                res = parser.parse(sentence)
                mistake += len(res['corrections'])

            # formula: (score = 100% - (mistake over total count times 100))
            score = 100-(mistake/word_count*100)

            self.__grammar_score = score
        return score

    def rate(self, input_text_dir: str, time: float) -> float:
        '''
            Formula:
            - Words / Time 
            - 140  to 160 wpm [ideal]
            - 2.33 to 2.67 score 

            - Note: Lower is Slower and Higher is Faster
        '''
        with open(input_text_dir, 'r') as file:
            text: list[str] = file.readlines()

        if time <= 0 or text[0] == '':
            return 0

        words: int = self.__word_count(text)
        result = words / time

        self.__rate_raw_result = result
        result /= 2.67
        result *= 100

        score = result % 100 if result > 100 else result
        self.__rate_score = score

        return score

    def __identify_hertz(self, gender, min, max) -> int:
        ...

    def __identify_gender(self, input_file) -> str:
        # speech segmenter is for audio analysis
        seg = Segmenter(vad_engine='sm')

        # by default gender dection is true, else set it to detect_gender=False
        segmentation = seg(input_file)
        gender = ['male', 'female']
        _gender = ''

        for s in segmentation:
            if gender[0] == s[0]:
                _gender = s[0]
                break
            if gender[1] == s[0]:
                _gender = s[0]
                break

        return _gender

    def test_identify_gender(self, audio):
        return self.__identify_gender(audio)

    def pitch(self, audio) -> float:
        '''
        identify pitch by hertz\n
        \n
        - for male   : [85  - 180]hz\n
        - for female : [165 - 255]hz\n
        \n
        Note: this can be seen in Spectrogram's 'Y-Axis'
        '''

        # # test, suppose audio is none this time
        m_hertz: list = [85, 180]  # m_hertz[0], m_hertz[1]
        f_hertz: list = [165, 255]  # f_hertz[0], f_hertz[1]

        # # identify the gender voice
        gender = self.__identify_gender(audio)

        score: int = 0

        hertz = self.__identify_hertz(gender, m_hertz[0], m_hertz[1]) if gender[0] == 'm' else self.__identify_hertz(
            gender, f_hertz[0], f_hertz[1])

        self.__pitch_score = score

        return score

    def articulation(self) -> None:
        '''
        Articulation
            Using MAR (Mean Articulatory Rate)
            10 - 20 consecutive syllables 

            Note: this is for fluent speech without pauses, MAR technique is a reliable approach for determining articulation rate.

            - dependent on words & voice
            - Using MAR (Mean Articulatory Rate)
        '''
        score = 0
        self.__articulation_score = score

    def prounounciation(self) -> None:
        '''
        Pronunciation
            Using Google Dictionary API

        - dependent on words & voice
        '''
        score = 0
        self.__prounounciation_score = score

    def volume(self) -> None:
        '''
        Volume
            Represented by Colours
            Low Volume  ??? Black to Red
            High Volume ??? Yellow to White

            Note: our group is still thinking if we are going to specify a specific speech distance when using the app

        dependent on voice & spectogram
        '''
        score = 0
        self.__volume_score = score

    # feedback

    def __get_total_avg_score(self) -> float:

        scores: dict = {
            'rate': self.__rate_score,
            'pitch': self.__pitch_score,
            'articulation': self.__articulation_score,
            'volume': self.__volume_score,
            'prounounciation': self.__prounounciation_score,
            'grammar': self.__grammar_score,
        }

        total_score = 0
        for index in scores:
            total_score += scores[index]
        return total_score / len(scores)

    def total_average_feedback(self):

        total_score: int = int(self.__get_total_avg_score())

        if total_score < 60:
            feedback = 'you did bad'
        elif total_score > 85:
            feedback = 'you did good'
        else:
            feedback = 'you need more practice'

        print(f'your total avg is: {total_score}%, so {feedback}')

    def get_total_average(self):
        return self.__get_total_avg_score()

    def __speed_comment(self) -> str:
        ideal = {'min': 2.33, 'max': 2.67}
        if self.__rate_raw_result > ideal['max']:
            return 'fast'
        if self.__rate_raw_result < ideal['min']:
            return 'slow'
        return 'ideal'

        return comment

    def __rate_feedback(self) -> str:
        speed = self.__speed_comment()
        score = self.__rate_score
        if score < 60:
            feedback = f"speech is {speed}"
        elif score > 85:
            feedback = f"speech is in the {speed} range"
        else:
            feedback = f"speech is {speed}"
        return feedback

    def __pitch_feedback(self, input_hz: float, min, max) -> str:
        if input_hz < min:
            return 'to low'
        if input_hz > max:
            return 'to to high'
        return 'keep it up'

    def __articulation_feedback(self) -> str:
        ...

    def __volume_feedback(self) -> str:
        ...

    def __pronunciation_feedback(self) -> str:
        ...

    def __grammar_feedback(self) -> str:
        ...

    def feedback_for(self, score_for: str, speed: float = 0) -> str:
        if score_for[0] == 'r':  # r - rate
            return self.__rate_feedback()
        if score_for[0] == 'p':  # p - pitch
            return self.__pitch_feedback(2, 1, 2)
        if score_for[0] == 'a':  # a - articulation
            return self.__articulation_feedback()
        if score_for[0] == 'v':  # v - volume
            return self.__volume_feedback()
        if score_for[0] == 'p':  # p - pronunciation
            return self.__pronunciation_feedback()
        if score_for[0] == 'g':  # g - grammar
            return self.__grammar_feedback()
        return 'could not return feedback'


class File:

    def __file_name(self) -> str:
        # uses: uuid, pytz, datetime
        todays: datetime = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
        utime: str = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

        deduct: int = -2 if str(todays.year)[1] == '0' else -3
        udate: str = f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"

        return f"{udate}{utime}"

    def generated_name(self) -> str:
        return f'{self.__file_name()}'

    def files_from_dataset(self, file_type) -> list:

        # add error handling
        file_list = []
        # get the directory above current directory then go to \audio\dataset
        path = os.path.abspath(os.path.join(
            os.getcwd(), os.pardir)) + '\\audio\\dataset'
        print("Current path:", path)
        for root, dirs, files in os.walk(path):
            for file in files:
                if file[-3:] == file_type:
                    file_list.append(os.path.join(root, file))
        return file_list
