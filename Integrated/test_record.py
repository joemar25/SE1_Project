from Recorder import Recorder

recorder = Recorder()

# record audio
print("start rec...")
record_file = recorder.record()
print("rec stop...")

# record[0] -> contains the audio & record[1] -> constains the frames
recorder.save(record_file['audio'], record_file['frames'])
