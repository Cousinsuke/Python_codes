#conditions, branching, SELECTION

#OPERATORS
#logical operators help us execute commands in specific circumstances

# == is equal to, != does not equal, <less than, >more than, >= more or equal, <= less or equal

#and, or, not

#boolean operators
#------------------
#and - two conditions are true
#or - either conditions is true
#not - the opposite is true

#binary selection
#------------------
'''
answer = 10
guess = int(input("what is 2X5?"))

if answer == guess:
    print("correct!")
else:
    print("corr...wrong!,loser")
'''
'''
answer2 = 30
guess2 = int(input("what is 5X6?"))

if answer2 == guess2:
    print("correct!")
else:
    print("corr...wrong!,loser")
'''
'''
answer3 = 3
guess3 = int(input("what is 2+1?"))

if answer3 == guess3:
    print("correct!")
else:
    print("corr...wrong!,loser")
'''

#case selection - multiple selection
#---------------

#''' - gives multi line print

dinner = input ('''
choose your dinner
1.chicken
2.fish
3.beef
''')

if dinner == "1":
    print ("You ordered chicken!")
elif dinner == "2":
    print ("You ordered fish!")
elif dinner == "3":
    print ("You ordered beef!")
else:
    print ("Not on menu")
  

#connected conditions
#---------------------
'''
name = input("Enter your name")
permitted = True

if name == "Bob"or name == "Luke" or name == "Josh" and permitted == True:
    print ("Access granted")
else:
    print ("Self destruct initiated")
'''
