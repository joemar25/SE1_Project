
    [/] makes the directory, if not exit - for saving the audio file

    [] from that audio files, the filenames would be save as list of dataset

    [] Gender Identification: Used for identify voice pitch
    <https://www.youtube.com/watch?v=ATCYEwSCGsE&ab_channel=DeepCode>

    question: pag malagom ang boses ng babae, or kung lalaki naman ay may pangbabae na boses

    [] (Mar) Articulation : to look further
    https://www.youtube.com/watch?v=xDTgziqNwSQ&ab_channel=SatyajitPattnaik




we use DRY aka Dont Repeat Yourself Principle in Programming


installation
conda install -c anaconda pyaudio
conda install -c anaconda portaudio
conda install -c pytorch pytorch
# required for whisper
conda install -c conda-forge tqdm
conda install -c conda-forge ffmpeg
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

# for inasegmenter
conda install -c conda-forge pydub
pip install inaSpeechSegmenter
