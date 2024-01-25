#======================================================================================================================================
#High score with dictionary
#======================================================================================================================================

from operator import itemgetter #

scores = { "Bob":21,
           "Ed":23,
           "Tony":45,     # this is the variable for names and score
           "Mary":116,
           "Gill":45,
           "Timmy":0}

sorted_scores = sorted(scores.items(), key = itemgetter(1), reverse = True) # this sorts the variable into 2 variable name and score
# and reverses the order 

print ("The first three high scores are:") 
for name,score in sorted_scores[:3]: # this is how many items gets printed 
    print(f'{name:10s}{score:d}') # s = string # d = double (64bit)


