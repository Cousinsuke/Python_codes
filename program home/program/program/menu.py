# Menu System
#----------------------

def menu():
    print('''
How would you like to be in the tournament?
1. press 1 for register
2. press 2 for add score
3. press 3 for score 
4. press 4 for high score
5. press 5 to quit
''')
    choice = input()
    if choice =="1":
        remenu()
    elif choice =="2":
        addscoremenu()
    elif choice =="3":
        scoremenu()
    elif choice =="4":
        gethiscore()
    elif choice =="5":
        quit()
    else:
        print("incorrect value")
        menu()

    
def remenu(): # register menu start
    print('''
How would you like to be in the tournament?
1. press 1 for team
2. press 2 for individual 
3. press 3 to quit
''')
    choice = input()
    if choice =="1":
        reteam()
    elif choice =="2":
        reindiv()
    elif choice =="3":
        quit()
    else:
        print("incorrect value")
        remenu()

    
def reteam():
    retname = input("enter your team name.")
    with open("teamregister.txt","a") as teamregister:
        teamregister.write(retname+",""\n")
def reindiv():
    reiname = input("enter your name.")
    with open("indivregister.txt","a") as indivregister:
        indivregister.write(reiname+",""\n")
def quit():
    print("You have pressed quit")
    menu()                                       # end of register menu
def addscoremenu(): #start of add score menu
    print('''
Whos score do you want to add?
1. press 1 for team
2. press 2 for individual 
3. press 3 to quit
''')
    choice = input()
    if choice =="1":
        addteam()
    elif choice =="2":
        addindiv()
    elif choice =="3":
        quit()
    else:
        print("incorrect value")
        addscoremenu()

    
def addteam():
    addtname = input("enter your team name.")
    addtscore = input("enter your score")
    with open("teamscore.txt","a") as teamscore:
        teamscore.write(addtname+","+addtscore+"\n")
def addindiv():
    addiname = input("enter your name.")
    addiscore = input("enter your score")
    with open("indivscore.txt","a") as indivscore:
        indivscore.write(addiname+","+addiscore+"\n")
def quit():
    print("You have pressed quit")
    menu()                #end of add score menu
def scoremenu():  #start of score menu
    print('''
Whos score do you want to see?
1. press 1 for team
2. press 2 for individual 
3. press 3 to quit
''')
    choice = input()
    if choice =="1":
        scteam()
    elif choice =="2":
        scindiv()
    elif choice =="3":
        quit()
    else:
        print("incorrect value")
        scoremenu()

    
def scteam():                                     ###
    gettscores = [] #team score
    with open('teamscore.txt') as theFile:
        for line in theFile:
            tname,tscore = line.strip().split(",")
            gettscores.append((tname,int(tscore)))

        sorted_scores = sorted(gettscores, key = lambda x: x[1],reverse = True)

    print ("all of teams score")
    for i in sorted_scores[:4]:
        print (i)                             #####
def scindiv():
    getiscores = [] #idividual score       ######
    with open('indivscore.txt') as theFile:
        for line in theFile:
            tname,tscore = line.strip().split(",")
            getiscores.append((tname,int(tscore)))

        sorted_scores = sorted(getiscores, key = lambda x: x[1],reverse = True)

    print ("all of idividual score")
    for i in sorted_scores[:20]:
        print (i)                    #####
def quit():
    print("You have pressed quit")
    menu()                    # end of score menu
def gethiscore(): # start of get high score menu
    print('''
Whos score do you want to see?
1. press 1 for team
2. press 2 for individual
3. press 3 to quit 
''')
    choice = input()
    if choice =="1":
        getteam()
    elif choice =="2":
        getindiv()
    elif choice =="3":
        quit()
        
    else:
        print("incorrect value")
        gethiscore()

    
def getteam():
    thiscores = [] #team high score
    with open('teamscore.txt') as theFile:
        for line in theFile:
            gettname,gettscore = line.strip().split(",")
            thiscores.append((gettname,int(gettscore)))

        sorted_scores = sorted(thiscores, key = lambda x: x[1],reverse = True)

    print ("The first 3 scores are:")
    for i in sorted_scores[:3]:
        print (i)
def getindiv():
    ihiscores = [] #team high score
    with open('indivscore.txt') as ihiscore:
        for line in ihiscore:
            getiname,getiscore = line.strip().split(",")
            ihiscores.append((getiname,int(getiscore)))

        sorted_scores = sorted(ihiscores, key = lambda x: x[1],reverse = True)

    print ("The first 3 scores are:")
    for i in sorted_scores[:3]:
        print (i)
def quit():
    print("You have pressed quit")
    menu()                  # end of get high score menu
def quit():
    print("You have pressed quit")
    menu()


while True:
    menu()