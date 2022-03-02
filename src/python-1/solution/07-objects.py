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

# 4: Vectors can be added, this will return a new vector
#    Example: V1 + V1 -> Vector(2,4,6)

# 5: Refactor/Extend code so that V1.add(Vector(2,3,4)) will mutate V1.
# We do not wat to see dublicated code. Remember: use deepcopy to clone an object

from copy import deepcopy

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z

    def __str__(self):
        return f"Vector({self.x, self.y, self.z})"

    def __add__(self, o):
        newV = deepcopy(self)
        newV.add(o)
        return newV

    def add(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z 
    

# Test the cases:
V1 = Vector(1,2,3)
V2 = Vector(2,3,4) # Expected output:
print(V1)          # Vector((1, 2, 3)) 
print(V1 + V2)     # Vector((3, 5, 7))
print(V1)          # Vector((1, 2, 3))
print(V2)          # Vector((2, 3, 4))
