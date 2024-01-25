iname = input("enter your name.")
iscore = input("enter your score")
with open("indivscore.txt","a") as indivscore:
    indivscore.write(iname+","+iscore+"\n")