###########################################
# Exercise: Wordle                        #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################
from random import randint


# Or use this:
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
    allWords = []
    with open(path, "r") as f:
        for line in f:
            word = line.strip().lower()
            allWords.append(word)
    return allWords

def allowedGuess(allWords, guess):
    """
    Check if guess is allowed (length = 5 and in wordlist) 
    Input:
        allWords: List of str
        guess: str
    Returns:
        Boolean
    """
    if not len(guess) == 5:
        return False
    if not guess in allWords:
        return False
    return True

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
    matches = ""
    for i, c in enumerate(guess):
        if c == trueWord[i]:
            matches += greenCube
        elif c in trueWord:
            matches += yellowCube
        else:
            matches += whiteCube
    return matches

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
        print(f"Looser! The word was {trueWord}")

if __name__ == "__main__":
    main()
