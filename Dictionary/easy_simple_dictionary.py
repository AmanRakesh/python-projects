import json
import sys

# variables
creator = "Aman"

# load the json file
jsonData = None
try:
    with open("dictionary.json", 'r') as jsonFile:
        jsonData = json.load(jsonFile)

except Exception as e:
    print(f"Error occurred while loading the json file. Reason: {e}")
    sys.exit(0)

# start the menu for the user
print(f"Welcome to the Awesome Dictionary made by yours truly {creator}\n")

while(True):
    word = input("enter a word: ")
    if word.upper() in jsonData.keys():
        meaning = jsonData[word.upper()]
        print(f"The meaning of the word {word} is \n{meaning}")
    else:
        print("OOPS!! My stupid creator didn't add this word and it's meaning :~(")
        print("However, You can add the meaning now if you like, and I will remember it :-)")
        response = int(input("1. Add the meaning\n2. If the creator didn't add it, why should I? I won't!\nresponse: "))
        if(response == 1):
            answer = input("Please type the meaning of the word here: ")
            jsonData[word.upper()] = answer
            print("Thank you for increasing my knowledge!")
            a = int(input('Press 0 to exit, any other number to search for another word: '))
            if(a == 0):
                break
    print("\n\n")

f = open("dictionary.json", 'w')
json.dump(jsonData, f, indent=4)
