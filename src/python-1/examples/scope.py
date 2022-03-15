# Usage of globals is fine.
def useX(y):
    return y + x # reffering to global x (10)

"""
# Not possible.
# The assignment of x forces that x is a local variable
def modifyX(y):  
    x = y + x
"""

x = 10
print(f"x at position 1: {x}")

y = useX(5)
print(f"y at position 1: {y}")

############################################

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print(f"x in g: {x}")
    h()
    return x

x = 3
print(f"x at position 2: {x}")
z = g(x)
print(f"z at position 1: {z}")

