#======================================================================================================================================
#High scores two ways
#txt files and dictionaries
#======================================================================================================================================

#txt files
hscores = []
with open ("Scores.txt") as file:
    for line in file:
        name,score = line.strip("\n").split(",")
        hscores.append((name, int(score)))

    sort_scores = sorted(hscores, key =lambda x: x[1], reverse = True)

    print ("The first three top score are:")
    for i in sort_scores[:3]:
        print (i)
