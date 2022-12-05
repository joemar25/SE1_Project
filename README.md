# SE1 Project

This Repository is for our Group project in our Software Engineering 1

Folders

- Unintegrated (test)
  - a folder contains pure python programs which is not yet integrated on the web
- Integrated (test)
  - a folder contains the (unintegrated python final codes) that is implemented on the web

---

## Library used

- [Whisper](<https://github.com/openai/whisper>)

  - used for speech recognition with speech to text feature
  - a lot of dataset for transcribing different languages
  - dependency: `ffmpeg`

    ```py
      # on Windows using Chocolatey (https://chocolatey.org/)
      # cmd must run (admin)
      choco install ffmpeg
    ```

    ```py
    # install whisper
    pip install git+https://github.com/openai/whisper.git 
    # or 
    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    # and
    pip install setuptools-rust
    ```

- [Librosa](https://github.com/librosa/librosa)
  
  - A python package for music and audio analysis
  - dependency: `soundfile` and `audioread`
  
  ```py
    # install librosa
    python -m pip install librosa
    # or 
    conda install -c conda-forge librosa
  ```

- [InaSpeechSegmenter](https://github.com/ina-foss/inaSpeechSegmenter)
  
  - A python package for music and audio analysis
  - dependency: `soundfile` and `audioread`
  
  ```py
    # install inaSpeechSegmenter
    pip install inaSpeechSegmenter
  ```

- [tmp](tmp)
  
  - note
  - dependency: `note`
  
  ```py
  # install
  ```
