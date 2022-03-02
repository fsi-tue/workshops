###########################################
# Exercise: Lists and Loops               #
#                                         #
# Introduction to Python programming      #
# by Jules Kreuer                         #
###########################################

# Goal: Understand how to uses lists


# E1:
# Print the last element of list l1
l1 = ["first", "middle", "last"]
print( l1[-1] )

# E2:
# Print every second element of list l2.
# Without loop.
l2 = [0,1,2,3,4,5,6,7,8,9]
print( l2[::2] )

# E3:
# Print the list l3 in reverse.
# Without loop.
l3 = [9,8,7,6,5,4,3,2,1,0]
print(list(reversed(l3)))
#or
print( l3[::-1] )

# E4 
# Print the element 4 to 8 in reverse order
l4 = [0,1,2,3,4,5,6,7,8,9]
print( l4[4:9:][::-1] )
#or 
print( l4[8:3:-1])

# E5
# Add the number 5 to l5.
l5 = [1,2,3,4]

# E6
# Add the content of l5 to l6
l6 = [-1,0]