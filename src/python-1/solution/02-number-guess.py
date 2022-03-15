###########################################
# Exercise: Guess the number              #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################

# Goal: Implement a basic python programme.
# 1. Generate a random number.
# 2. Ask for a guess.
# 3. Check if guess was correct.
# 4. If not, say if number was smaller / larger
# 5. Repeat from step 2, but only 8 times max.

# Hints:
#
# Function "randint(a,b)" from module "random" returns 
# a (pseudo)-random integer N such that a <= N <= b
# 
# Function input("Number?") will promt "Number?" and return 
# the user-input as string

from random import randint

def main():
    toGuess = randint(0, 1024)
    numberOfGuesses = 0

    while numberOfGuesses < 8:
        userGuess = input("Your guess:")
        userGuess = int(userGuess)

        if userGuess == toGuess:
            print("Congrats, you found it.")
            break
        else:
            numberOfGuesses += 1
            if userGuess < toGuess:
                print("The number is larger.")
            else:
                print("The number is smaller.")
    
    if numberOfGuesses == 7:
        print("Looser! The number was " + str(toGuess))

if __name__ == "__main__":
    main()
