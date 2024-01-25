tname = input("enter your team name.")
tscore = input("enter your score")
with open("teamscore.txt","a") as teamscore:
    teamscore.write(tname+","+tscore+"\n")