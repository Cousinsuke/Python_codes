gettscores = [] #team score
with open('teamscore.txt') as theFile:
    for line in theFile:
        tname,tscore = line.strip().split(",")
        gettscores.append((tname,int(tscore)))

    sorted_scores = sorted(gettscores, key = lambda x: x[1],reverse = True)

    print ("all of teams score")
    for i in sorted_scores[:4]:
        print (i)