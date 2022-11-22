# SE1 Project

This Repository is for our Group project in our Software Engineering 1

Folders

- Unintegrated (test)
  - a folder contains pure python programs which is not yet integrated on the web
- Integrated (test)
  - a folder contains the (unintegrated python final codes) that is implemented on the web

---

## Open Souce used

- [WHISPER](<https://github.com/openai/whisper>)

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
