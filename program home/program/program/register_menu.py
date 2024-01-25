# Register Menu System
#----------------------

def remenu():
    print('''
How would you like to be in the tournament?
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
        remenu()

    
def team():
    print("You have been entered in team")
def indiv():
    print("You have be entered as a individual")
def quit():
    print("You have pressed quit")
    remenu()

while True:
    remenu()