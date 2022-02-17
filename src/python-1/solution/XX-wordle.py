###########################################
# Exercise: Wordle                        #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################
from random import randint

# Use
from colorama import init
from termcolor import colored
init() 

greenCube  = colored(' ', 'green', 'on_green')
yellowCube = colored(' ', 'yellow', 'on_yellow')
whiteCube  = colored(' ', 'white', 'on_white')

# Or use this:
greenCube  = "🟩"
yellowCube = "🟨"
whiteCube  = "⬜"
###########################################
def loadWords(path):
    allWords = []
    with open(path, "r") as f:
        for line in f:
            word = line.strip().lower()
            allWords.append(word)
    return allWords

def matchGuess(trueWord, guess):
    matches = ""
    for i, c in enumerate(guess):
        if c == trueWord[i]:
            matches += greenCube
        elif c in trueWord:
            matches += yellowCube
        else:
            matches += whiteCube
    return matches

def allowedGuess(allWords, guess):
    if not len(guess) == 5:
        return False
    if not guess in allWords:
        return False
    return True

def main():
    # Load all Words
    allWords = loadWords("words.txt")
    # Pick one
    trueWordPosition = randint(0, len(allWords)-1)

    trueWord = allWords[trueWordPosition]

    numberOfGuesses = 0
    print(f"\t {0}: {whiteCube*5}")
    while numberOfGuesses < 6:
        # Aks for guess
        guess = input("Your guess: ")
        guess = guess.strip().lower()
        # If valid guess
        if allowedGuess(allWords, guess):
            numberOfGuesses += 1
            match = matchGuess(trueWord, guess)
            print(f"\t {numberOfGuesses}: {match}")
            if guess == trueWord:
                print("Congratulations")
                break
        else:
            print("Invalid guess. Try again!")
    else:
        print("Looser")

if __name__ == "__main__":
    main()
