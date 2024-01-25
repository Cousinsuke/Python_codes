'''
name = "bobby"

name  = name.upper()#capitalises the whole name
print (name)
name = name.lower()#whole name is lower case
print (name)
lenghtName = len(name)#tell you how many letters in the name
print (lenghtName)
caps = name.capitalize()#capitalise the first letter
print (caps)
'''
'''
name = "Sam Tarly" 

s1 = slice(3) 
print(s1)
print (name[s1])
#The stop valueis one MORE than the last value in the slice

s2 = slice(1, 5, 2)
print (name[s2])

s3 = slice(-1, -9, -2)
print (name[s3])
'''
'''
email = "James123@yahoo.com"
Fname = slice(0, 5)
print (email[Fname])

Prov = slice(9, 14)
print (email[Prov])

Dom = slice(8, 9)
print (email[Dom])
'''
'''
b = "hello, World!"
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])

print(b[-8:-2:2])
'''
'''
email = "James123@yahoo.com"
print (email[0:5])

print (email[9:14])

print (email[8:9])
'''
'''
#replace
a = "Hello, World!"
print(a.replace("H", "J"))
'''
'''
#split
a = "Hello, World!"
print(a.split(",")) #returns ['Hello', 'World!']
'''
'''
#find
sentence = "You know nothing Jon Snow"
word = input("Enter the word to find")
position = sentence.find(word)
print("The word",word,"is at character",position)
'''
'''
#replace
a = "James123@yahoo.com"
print(a.replace("123", "456"))
'''
'''
#find
a = "James123@yahoo.com"
word = input("Enter the word to find")
position = a.find(word)
print("The word",word,"is at character",position)
'''



