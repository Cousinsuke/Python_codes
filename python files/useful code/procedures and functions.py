#procedures and functions
#-------------------------

#procedure - mini program - no returns - useful to avoid repetition
'''
def xVal():
    x = 10
    t = x*x
    print (t)

xVal()
'''

#function - same as procedure but has return
''' 
def xVal():
    x = 10
    t = x*x
    return t

total = xVal()
print (total)
'''

#parameters - data you send in to procedures and functions
'''
num1 = 15
num2 = 12

dog = 2
cat = 15

def numCruncher(x,y): # told it to expect 2 parameters
    z = x*y
    return z

total = numCruncher(num1,num2)
print (total)

total = numCruncher(dog,cat)
print (total)
'''

#make a function that takes in a name
#counts how many letters in the name
#returns the number of letters
#outputs that to the user

#without parameter
'''
def countit():
    name = input("enter a name")
    lenName = len(name)
    return lenName

nameCount = countit()
print(nameCount)
'''
#with parameter input

name = input("enter a name")
def countit(name):
    lenName = len(name)
    return lenName

nameCount = countit(name)
print(nameCount)
