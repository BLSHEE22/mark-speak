import random
import sys
import os

### RUNNING INSTRUCTIONS

### python3 boolsayn.py 'text_filename' 'number_of_die_sides'

### FILENAME OPTIONS

### fgp.txt
### tijSun.txt
### shineOn.txt
### Feel free to add your own text files to your local repo!

### OPTIONS FOR NUMBER OF DIE SIDES

### 2 - every available word is replaced!
### 3 - a randomly chosen two-thirds of available words are replaced.
### 4 - a randomly chosen half of available words are replaced.
### ...
#### X - a randomly chosen two out of X of available words are replaced.

#GLOBALS
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
transWeights = ["2 - every available word is replaced!","3 - a randomly chosen two-thirds of available words are replaced.",
                "4 - a randomly chosen half of available words are replaced.","5 - a randomly chosen two-fifths of available words are replaced.",
                "...","X - a randomly chosen two out of X available words are replaced."]
artpro = ["a", "an", "and", "the", "i", "i'm", "i've", "i'll", "you", "you're", "you've", "me", "my", "he", "he's", "she", "she's", "we", "we're", "we've", "they", "they're", "they've", "them", "him", "her", "your," "their", "it", "its", "it's"]
prepos = ["abroad", "about", "above", "across", "after", "against", "ahead", "along", "amidst", "among", "amongst", "apart", "around", "as", "because", "before", "but", "in", "into", "like", "next", "of", "off", "on", "to", "from"] 
verbs = ["not", "is", "isn't", "are", "aren't", "was", "wasn't", "were", "weren't", "will", "won't", "has", "hasn't", "have", "haven't", "been", "what's", "did", "didn't", "could", "couldn't", "should", "shouldn't", "would", "wouldn't"]
adj = ["who", "what", "where", "when", "why", "how", "little", "big", "numerous", "out", "top", "bottom"]
adv = ["just"]

def read_data(fname):
    exemplars = []
    file = open(fname)
    words = []
    for line in file:
        words += line.split()

    return words

def rollDX(words, x):
    i = 1
    newWords = []
    words = ["\n" if y == "\\n" else y for y in words]
    #print(words)
    for word in words:
        newWord = ""
        nonAlNum = ""
        for let in word:
            if let.isalnum():
                newWord += let
            else:
                nonAlNum += let
        if newWord != "" and "'" not in nonAlNum and "\"" not in nonAlNum and "-" not in nonAlNum and newWord.lower() not in artpro and newWord.lower() not in prepos and newWord.lower() not in verbs and newWord.lower() not in adj and newWord.lower() not in adv:
            roll = random.randint(1, x)
            if roll == x - 1:
                if i == 1:
                    if len(newWord) == 1:
                        newWord = "."
                    elif len(newWord) > 3:
                        if newWord[-1] == "s":
                            newWord = "Bools"
                        elif newWord[-2] == "e" and newWord[-1] == "d":
                            newWord = "Booled"
                        elif newWord[-3] == "i" and newWord[-2] == "n" and newWord[-1] == "g":
                            newWord = "Boolin"
                        else:
                            newWord = "Bool"
                    else:
                        newWord = "Bool"
                    newWord += nonAlNum
                else:
                    if len(newWord) == 1:
                        newWord = "."
                    elif len(newWord) > 3:
                        if newWord[-1] == "s":
                            newWord = "bools"
                        elif newWord[-2] == "e" and newWord[-1] == "d":
                            newWord = "booled"
                        elif newWord[-3] == "i" and newWord[-2] == "n" and newWord[-1] == "g":
                            newWord = "boolin"
                        else:
                            newWord = "bool"
                    else:
                        newWord = "bool"
                    newWord += nonAlNum
            elif roll == x:
                if i == 1:
                    if len(newWord) == 1:
                        newWord = "."
                    else:
                        if newWord[-1] == "s":
                            newWord = "Sayns"
                        elif newWord[-2] == "e" and newWord[-1] == "d":
                            newWord = "Sayned"
                        else:
                            newWord = "Sayn"
                    newWord += nonAlNum
                else:
                    if len(newWord) == 1:
                        newWord = "."
                    else:
                        if newWord[-1] == "s":
                            newWord = "sayns"
                        elif word[-2] == "e" and newWord[-1] == "d":
                            newWord = "sayned"
                        else:
                            newWord = "sayn"
                    newWord += nonAlNum
            else:
                newWord = word
        else:
            newWord = word
        if "." in newWord or "?" in newWord or "!" in newWord:
            i = 0
        # print(newWord)
        newWords.append(newWord)
        i += 1

    return newWords

def main():
    fileAsk = OKBLUE + "\nWelcome to the Mark-Speak Translator!" + WARNING + "\n\nChoose a file that you want translated.\n\n" + ENDC
    entries = os.listdir("texts")
    for x in [y for y in entries if not y == ".DS_Store"]:
        fileAsk += x + "\n"
    fileAsk += "\n"
    fileAns = input(fileAsk)
    transAsk = WARNING + "\nYou have chosen \"" + fileAns + ".\"\n\nNext, choose a translation setting. Options are from 2 and up.\n\n" + ENDC
    transAsk += f"Words that CANNOT be replaced: {artpro + prepos + verbs + adj + adv} \n\n"
    for x in transWeights:
        transAsk += x + "\n"
    transAsk += "\n"
    transAns = input(transAsk)
    print(WARNING + "\nYou have chosen option \"" + transAns + ".\" Converting " + fileAns + " to mark-speak with translation weight of 2/" + transAns + "...\n")
    wordsToBeChecked = read_data("texts/" + fileAns)
    result = rollDX(wordsToBeChecked, int(transAns))
    print(OKGREEN + "Here is your translation:\n" + ENDC)
    for x in result:
        print(x + " ", end="")
    print("\n")

if __name__ == "__main__":
    main()