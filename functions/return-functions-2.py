'''
Program to demonstrate the use of passing parameters with return statements in Python
Hussein Elguindi
'''

def isBiggerThan(a, b): # arguments a and b to be compared
    if a > b: # check if a is bigger than b
        return str(a) + " is bigger than " + str(b) # return string
    elif a < b: # check is a is less than b
        return str(b) + " is bigger than " + str(a) # return string
    else: # check if a is the same as b
        return str(a) + " is the equal to " + str(b) # return string

def isLessThan(a, b):
    if a < b:
        return str(a) + " is less than " + str(b)
    elif a > b:
        return str(b) + " is less than " + str(a)
    else:
        return str(a) + " is the equal to " + str(b)

print(isBiggerThan(1, 2)) # call bigger than function with 1 and 2 as parameters
print(isLessThan(1, 2))
print(isBiggerThan(2, 2))