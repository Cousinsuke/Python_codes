#=======================================================================================================================================
#high score write to file
#======================================================================================================================================
scores = []
with open('results.txt') as theFile:
    for line in theFile:
        name,score = line.strip().split(",")
        scores.append((name,int(score)))

    sorted_scores = sorted(scores, key = lambda x: x[1],reverse = True)

    print ("The first 5 scores are:")
    for i in sorted_scores[:5]:
        print (i)

