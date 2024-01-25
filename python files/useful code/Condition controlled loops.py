#condition controlled loops
#----------------------------

#syntax
#while expression:
    #statement(s)

#condition loops will run until the condition is met.
#RECURSION - the loop goes on forever
'''
while True:
    print ("I am Awesome")
'''
'''
count = 0
while count < 5:
    print ("the count is :", count)
    count +=1
'''

#task - make a countdown loop using a while loop

import time
'''
counter = 11
while counter != 0:
    counter -=1
    time.sleep(1)
    print(counter)

print("BOOM!")
'''
'''
a = [1,2,3,4]

while a:
    print(a.pop()) # to this do this()
'''
#-------------------------------------------------
    
x = 10
y = 1

while x>y:
    print (x*y)
    y+=1
else:
    print("finished")

#task - turn this into pseudocode
'''
START

x = 10
y = 1

WHILE x>y THEN
    PRINT x*y
    y+=1
ELSE
    PRINT finished
END WHILE

END
'''
