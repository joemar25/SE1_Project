import glob

# absolute path to search all text files inside a specific folder
path = r'audio\dataset\*.txt'

for file in glob.glob(path, recursive=True):
    print(file)
