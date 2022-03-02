class Counter():
    def __init__(self, x):
        self.x = x
        self.origin = x

    def addOne(self):
        self.x = self.x + 1

    def removeOne(self):
        self.x = self.x - 1
    
    def reset(self):
        self.x = self.origin

print("Init")
c = Counter(0)

print(f"{c.x=}")
print(f"{c.origin=}")

print("Add one")
c.addOne()

print(f"{c.x=}")
print(f"{c.origin=}")

print("Reset")
c.reset()

print(f"{c.x=}")
print(f"{c.origin=}")

