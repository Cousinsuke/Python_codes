iname = input("enter your team name.")
with open("indivregister.txt","a") as indivregister:
    indivregister.write(iname+",""\n")