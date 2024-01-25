#---------------------------------------------------------------------
#Name:       dodgy dealers 1

#
# 1. open a list to read from
# 2. use a for loop to read through each line
# 3. strip and split the line
# 4. make a new list to get intergers to work with
# 5. format the lines to print nicely

#------------------------------------------------------------------
littleList = []
bigList = []

Oldest = 2023

# open read file
theFile = open ("Vehicle details10.txt", "r")

# loop over each line in the file

for theLine in theFile:
    theLine = theLine.strip("\n") # strip the newline
    theSplitLine = theLine.split(",")
    littleList = []
    littleList.append(theSplitLine[0])
    littleList.append(int(theSplitLine[1]))
    littleList.append(theSplitLine[2])
    littleList.append(theSplitLine[3])
    littleList.append(int(theSplitLine[4]))
    bigList.append(littleList)

# format a table    
# {} make a cell,  < ^ > justify text , size of the cell
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))

for item in bigList:
    print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(item[0],item[1],item[2],item[3],item[4]))

# SEARCH FOR THE OLDEST
'''
Oldest = 2023
for item in bigList:
    if item[1] <Oldest:
        Oldest = item[1]
        TheOldest = item

print ('The oldest car is: ')
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(TheOldest[0],TheOldest[1],TheOldest[2],TheOldest[3],TheOldest[4]))
#SEARCH FOR THE NEWEST

Newest = 1950
for item in bigList:
    if item[1] >Newest:
        Newest = item[1]
        TheNewest = item

print ('The newest car is: ')
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(TheNewest[0],TheNewest[1],TheNewest[2],TheNewest[3],TheNewest[4]))
# SEARCH FOR THE CHEAPEST

Cheapest = 20000
for item in bigList:
    if item[4] <Cheapest:
        Cheapest = item[4]
        TheCheapest = item

print ('The cheapest car is: ')
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(TheCheapest[0],TheCheapest[1],TheCheapest[2],TheCheapest[3],TheCheapest[4]))
# SEARCH FOR THE MOST EXPENSIVE

MExpensive = 100
for item in bigList:
    if item[4] >MExpensive:
        MExpensive = item[4]
        TheMExpensive = item

print ('The most expensive car is: ')
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(TheMExpensive[0],TheMExpensive[1],TheMExpensive[2],TheMExpensive[3],TheMExpensive[4]))
'''
#sort the biglist - by any of the index values

#tothis, do this, like this, function, one argument

bigList.sort(key = lambda x: x[4], reverse = True)
print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format("MODEL","YEAR","COLOUR","CONDITION","PRICE"))

for item in bigList:
    print('{:<10}{:<4}{:^10}{:^10}{:>6}'.format(item[0],item[1],item[2],item[3],item[4]))
