__authors__ = "joemar_olan_glenn_arrlee_jericho"
__version__ = "1.5"
__docformat__ = "restructuredtext en"

try:
    import os
    from Generator import Score
    from Recorder import Recorder
except ImportError as e:
    print(e)
    raise


def main():
    # ######################## object instances ######################### #

    check = Score()
    recorder = Recorder()

    # ############################ recording ########################### #

    print("start rec...")
    record_file = recorder.record()
    print("rec stop...")

    # ############################## save ############################## #

    s_audio = record_file['audio']
    s_frames = record_file['frames']

    recorder.save(s_audio, s_frames)

    # ####### get audio specific data from the specific instance ######## #

    txt_file: str = recorder.get_txt_file_name()
    wav_file: str = recorder.get_wav_file_name()
    audio_duration: float = recorder.get_audio_duration(wav_file)

    # ############################# scores ############################## #

    grammar_score: float = check.grammar(txt_file)
    speed_score: float = check.rate(txt_file, audio_duration)

    # ############################# detatils ############################ #

    os.system('cls')
    print('\nscores')
    print(f'rate score     : {speed_score}')
    print(f'grammar score  : {grammar_score}')

    # ############################# overall ############################ #

    print('total average   : %.1f' % check.get_total_average())
    print('\nfeedbacks\nrate :', check.feedback_for('rate'), end='\n\n')


if __name__ == "__main__":
    main()
