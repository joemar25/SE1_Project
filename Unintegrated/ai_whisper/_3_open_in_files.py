from colorama import Fore
import colorama
from textblob import TextBlob

text_source = './audio/dataset/221123e2754261-6b34-11ed-ab15-708bcd015b0c13440.txt'

# open text file and read it and save to data
with open(text_source, 'r') as file:
    data = file.readlines()

# remove \n
data = [i.strip() for i in data]


colorama.init(autoreset=True)
t = TextBlob('test si good')
c = t.correct()
print("correct text is:")
print(Fore.RED+str(c))
