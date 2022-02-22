def useX(y):
  return y + x
		
def modifyX(y):  
  x = y + x

x = 10
y = useX(5)
modifyX(y)
print(x)
