#Iteration
#-----------
# An iteration is a section of code that is repeated.
#Iterations are also known as loops.
#Counter controlled iteratios are used when you want to iterate a known number of times.

#Code must be indented within an iteration.
#It would be good practice to comment code before aniteration to explain what is happening.

#One 'for' loops can be put inside another 'for' loop. This is known as meeting.

'''
for counter in range(0,5): #counter is a temp variable for this loop
    print(counter)
'''
'''
for counter in range(0,11,2):
    print(counter)
'''
'''
for counter in range(10,0,-1):  #(start,end,step)
    print(counter)
'''
'''
import time
for counter in range(10,-1,-1):
    time.sleep(1)
    print(counter)
    if counter == 0:
        print("BOOM!")
'''
    #input  0          1         2
fruits = ["apple", "banana", "cherry"]
'''
for x in fruits:
    print(x)
'''
'''
for x in fruits:
    print(x)
    if x == "banana":
        break
'''

#task = make a list of names
#put the name bob in there
#create a loop to find bob
#stop the loop when it finds bob

'''
for x in range(6):
    print(x)    #what is the last value printed? 5
'''
'''
for x in range(2, 6):
    print(x)
'''
'''
for x in range(2, 30, 3):
    print(x)
'''
'''
fruits = ["apple", "banana", "cherry"]
for x in range (len(fruits)):
    print(x) #what gets printed? prints the index value
'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
