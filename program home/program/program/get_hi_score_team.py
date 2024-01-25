thiscores = [] #team high score
with open('teamscore.txt') as theFile:
    for line in theFile:
        tname,tscore = line.strip().split(",")
        thiscores.append((tname,int(tscore)))

    sorted_scores = sorted(thiscores, key = lambda x: x[1],reverse = True)

    print ("The first 3 scores are:")
    for i in sorted_scores[:3]:
        print (i)