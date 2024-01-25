#Menu System
#------------

def menu():
    print('''
Tell me what you want to do?
1. Hit 1 to Bop it!
2. Hit 2 to twist it!
3. Hit 3 to pull it!
4. Hit 4 to shake it!
5. Hit 5 to quit it!
''')
    choice = int(input())
    if choice ==1:
        bopit()
    elif choice ==2:
        twistit()
    elif choice ==3:
        pullit()
    elif choice ==4:
        shakeit()
    elif choice ==5:
        print("bye then")
    else:
        print("incorrect value")
        menu()

    
def bopit():
    print("Bop it!")
def twistit():
    print("twist it!")
def pullit():
    print("pull it!")
def shakeit():
    print("shake it!")
def quitit():
    print("bye then")

while True:
    menu()


