# Score Menu System
#----------------------

def scoremenu():
    print('''
Whos score do you want to see?
1. press 1 for team
2. press 2 for individual 
3. press 3 to quit
''')
    choice = int(input())
    if choice ==1:
        team()
    elif choice ==2:
        indiv()
    elif choice ==3:
        quit()
    else:
        print("incorrect value")
        scoremenu()

    
def team():
    print("Teams score")
def indiv():
    print("Individuals score")
def quit():
    print("You have pressed quit")
    scoremenu()

while True:
    scoremenu()