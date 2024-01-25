tname = input("enter your team name.")
with open("teamregister.txt","a") as teamregister:
    teamregister.write(tname+",""\n")