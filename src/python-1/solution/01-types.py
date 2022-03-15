###########################################
# Exercise: Types                         #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################

# Goal: Understand the different types and type-casting in python.
# Desired output: "The sum of 41.8 and 0.2 is 42".

# Use following variables.
f1 = 41.8
f2 = 0.2
prefix = "The sum of "

sentence = prefix + str(f1) + " and " + str(f2) + " is " + str(f1+f2)

# Alternative with f-strings
sentence = f"{prefix}{f1} and {f2} is {f1+f2}"

print(sentence)
