ihiscores = [] #team high score
with open('indivscore.txt') as ihiscore:
    for line in ihiscore:
        iname,iscore = line.strip().split(",")
        ihiscores.append((iname,int(iscore)))

    sorted_scores = sorted(ihiscores, key = lambda x: x[1],reverse = True)

    print ("The first 3 scores are:")
    for i in sorted_scores[:3]:
        print (i)