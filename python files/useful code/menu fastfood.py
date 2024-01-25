def menu():
    print('''
Tell me what you want?
 input number 1-5
1. curry
2. burger
3. icecream
4. hotdog
5. fish and chips
''')
    choice = int(input())
    if choice ==1:
        curry()
    elif choice ==2:
        burgert()
    elif choice ==3:
        icecream()
    elif choice ==4:
        hotdog()
    elif choice ==5:
        fishandchips ()
    else:
        print("incorrect value")
        menu()

def curry():
    print("you ordered curry")
def burger():
    print("you ordered burger")
def icecream():
    print("you ordered icecream")
def hotdog():
    print("you ordered a hotdog")
def fishandchips():
    print("you ordered fish and chips")

while True:
    menu()        
