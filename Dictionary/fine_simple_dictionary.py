#imports
from importlib.resources import path
import json
import sys
from isort import file

#variables
creator = "Aman"
path_to_dictionary_file = "dictionary.json"
jsonData = None

# load the json file


def loadDictionaryJson(path_to_dictionary_file):
    data = {}
    try:
        with open(path_to_dictionary_file, 'r') as jsonFile:
            data = json.load(jsonFile)

    except Exception as e:
        print(f"Error occurred while loading the json file. Reason: {e}")
        
    return data

#dump the json data
def dumpJsonData(filepath, jsonData):
    print("dumping json data to add additional values")
    f = open(filepath, 'w')
    json.dump(jsonData, f, indent=4)

def getMeaningOfWord(jsonData, word):
    meaning = None
    if word.upper() in jsonData.keys():
        meaning = jsonData[word.upper()]

    return meaning        

def exitProcess(filepath, jsonData):
    dumpJsonData(filepath, jsonData)
    sys.exit(0)

# start the process for the user
def processStart(jsonData, path_to_dictionary_file):

    print(f"Welcome to the Awesome Dictionary made by yours truly {creator}\n")
    while(True):
        word = input("enter a word: ")
        meaning = getMeaningOfWord(word, jsonData)
        if meaning!=None:
            print(f"The meaning of the word {word} is \n{meaning}")
        else:
            print(
                "OOPS!! My stupid creator didn't add this word and it's meaning :~(")
            print("However, You can add the meaning now if you like, and I will remember it :-)")
            response = int(input(
                "1. Add the meaning (if you know obviously xD)\n" +
                "2. If the creator didn't add it, why should I? I won't!\n" +
                "3. Exit\n"
                "response: "))
            if response == 3:
                exitProcess(jsonData, path_to_dictionary_file)

            elif response==2:
                continue

            elif response == 1:
                answer = input("Please type the meaning of the word here: ")
                jsonData[word.upper()] = answer
                print("Thank you for increasing my knowledge!")
        print("\n\n")

if __name__ == "__main__":
    jsonData = loadDictionaryJson(path_to_dictionary_file)
    processStart(jsonData, path_to_dictionary_file)

