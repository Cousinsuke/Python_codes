#lambda
#-------

#lambda - on the fly function - nameless
#can take any number of arguments (parameter) but returns only one expression

'''
x = lambda a : a +10

print ( x(5) )

x = lambda a,b : a*b

print ( x(5,7) )

x = lambda a,b,c : (a*b)+c

print ( x(5,7,9) )
'''



# what is going on?
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(5)
print(mydoubler(11))
