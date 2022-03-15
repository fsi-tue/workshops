###########################################
# Exercise: Guess the number              #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################

# Goal: Understand functions

# E1
# Implement a function that takes no paramter and returns true

def alwaysTrue():
    return True

# E2 
# Implement a function that takes a list l, an int i and a string s.
# Return the value at the i-th position of l.
# If i is too large return s.

def defaultIndex(l, i, s):
    if i < len(l):
        return l[i]
    else:
        s

# E3 
# Implement a function that takes another function f and applies the number 5 to it.
# Return the value

def apply5(f):
    return f(5)

# E4 
# Import the module random and use the random function to print a random number.
import random 
print(random.random())

# E4 
# Import only the function randint
from random import randint