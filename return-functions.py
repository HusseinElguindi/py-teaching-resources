'''
Program to demonstrate the use of passing parameters with return statements in Python
Hussein Elguindi
'''

def add(a, b): # arguments a and b to be passed when calling the function
    result = a + b # calculate result and store in result variable
    return result # return the calculated result

def subtract(a, b):
    result = a - b
    return result

def divide(a, b):
    result = a / b
    return result

def multiply(a, b):
    result = a * b
    return result

print(add(1, 2)) # prints the addition of arguments 1 and 2
print(subtract(5, 2))
print(divide(10, 2))
print(multiply(2, 4))