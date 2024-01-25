getiscores = [] #idividual score
with open('indivscore.txt') as theFile:
    for line in theFile:
        tname,tscore = line.strip().split(",")
        getiscores.append((tname,int(tscore)))

    sorted_scores = sorted(getiscores, key = lambda x: x[1],reverse = True)

    print ("all of idividual score")
    for i in sorted_scores[:20]:
        print (i)