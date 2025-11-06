import requests
import json
import random

url = "https://api.datamuse.com/words?rel_jjb=ocean"
response = requests.get(url)
data = response.json() 

sentence = "The ocean is a vast and mysterious place because que it is "
count = 0
for item in data:
    randomIndex = random.randint(0, len(data)-1)
    sentence += data[randomIndex]["word"] + ", "
    count += 1
    if count == 5:
        break

print(sentence)
    



