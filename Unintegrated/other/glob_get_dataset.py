import glob

# absolute path to search all text files inside a specific folder
path = r'C:\Users\joema\Desktop\MamiTess\*.wav'

for file in glob.glob(path, recursive=True):
    print(file)
