import json
import sys
from difflib import get_close_matches

data = json.load(open("data.json"))

def funct(word):
    result = dict(word)
    if type(result) == list:
        for i in result:
            print(i)
    else :
        print(result)

def dict(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0 :
        yn = input("Did you mean %s instead? Enter Y if yes, N for no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n" :
            return "The word doesn't exist. Please double check it."
        else:
            return "Your entry was not valid."

    else:
        return "The word doesn't exist. Please double check it."

sys.stdout.write("\033[1;36m")
print("WELCOME TO SHREYANSH'S DICTIONARY")
print("REMEMBER!\nUSE \end TO EXIT THE DICTIONARY")
while True:
    word = input("Enter input : ")
    if word == "\end":
        break
    else:
        funct(word)