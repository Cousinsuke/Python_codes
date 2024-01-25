# Event Menu System
#----------------------

def eventmenu():
    print('''
What event are you in?
1. press 1 for swimming
2. press 2 for running
3. press 3 for cycling
4. press 4 for rowing
5. press 5 for fencing
''')
    choice = int(input())
    if choice ==1:
        swimming()
    elif choice ==2:
        running()
    elif choice ==3:
        cycling()
    elif choice ==4:
        rowing()
    elif choice ==5:
        fencing()
    else:
        print("incorrect value")
        eventmenu()

    
def swimming():
    print("You have press swimming")
def running():
    print("You have press running")
def cycling():
    print("You have press cycling")
def rowing():
    print("You have press rowing")
def fencing():
    print("You have press fencing")

while True:
    eventmenu()