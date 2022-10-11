###########################################
# Exercise: Objects  / Vectors            #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################

# Goal: Implement a Vector-Class with following properties:
# 1: Holds values for x, y, z
#    Example: V1 = Vector(1,2,3)

# 2: Two vectors are equal if all components are equal

# 3: Vectors can be printed in a nice way.

# 4: Vectors can be added, this will return a new vector.
#    Neither V1 nor V2 shall be altered.
#    Example: V1 + V1 -> Vector(2,4,6)

# 5: Refactor/Extend code so that V1.add(Vector(2,3,4)) will mutate V1.
#    We do not want to see duplicated code.

# 6: Exceptions: Add a check to prohibit negative numbers. Throw an exception if a negative number is used.

class Vector():

# Test the cases:
#V1 = Vector(1,2,3)
#V2 = Vector(2,3,4) # Expected output:
#print(V1)          # Vector((1, 2, 3)) 
#print(V1 + V2)     # Vector((3, 5, 7))
#print(V1)          # Vector((1, 2, 3))
#print(V2)          # Vector((2, 3, 4))
