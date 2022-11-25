#Importing tqdm function of tqdm module 
from tqdm import tqdm  
from time import sleep 
for i in tqdm(range(200)):  
# Waiting for 0.01 sec before next execution 
   sleep(.01)