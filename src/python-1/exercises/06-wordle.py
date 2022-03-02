###########################################
# Exercise: Wordle                        #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################
from random import randint

# Chose between 
from colorama import init
from termcolor import colored
init() 

greenCube  = colored(' ', 'green', 'on_green')
yellowCube = colored(' ', 'yellow', 'on_yellow')
whiteCube  = colored(' ', 'white', 'on_white')

# Or this:
greenCube  = "🟩"
yellowCube = "🟨"
whiteCube  = "⬜"
###########################################
def loadWords(path):
    """
    Load all word of file.
    Input:
        path: Str, path of file
    Returns:
        allWords: List of str.
    """
    return

def allowedGuess(allWords, guess):
    """
    Check if guess is allowed (length = 5 and in wordlist) 
    Input:
        allWords: List of str
        guess: str
    Returns:
        Boolean
    """
    return

def matchGuess(trueWord, guess):
    """
    Creates the Wordle representation of a guess:
    Green Cube for correct letter at correct position.
    Yellow Cube for correct letter at incorrect position.
    White Cube otherwise.

    Input: 
        trueWord: str, the word to guess
        guess: str, the actual guess
    Returns:
        match, str, Wordle representation.
    """
    return

def main():
    # Load all Words
    
    # Pick one
    
    # Print starting 
    print(f"\t {0}: {whiteCube*5}")

    # Enter loop
    
        # Aks for guess
        
        # If valid guess
            # print wordle representation
            # Check if guess was correct

if __name__ == "__main__":
    main()
