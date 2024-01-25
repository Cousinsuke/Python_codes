#*****************************
# Python Dictionaries
#*****************************
# dictionary - data structure composed of keys and values
# they are ORDERED - the order in which the data is held cannot change
# once you set the keys you cant change them
#****************************

# make a dictionary using curly brackets
# keys can be any simple data type
# Values can be any data type
thisdict = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964,
    "Driveable" : True,
    }

# outputting data

x = thisdict.values() # assign the values to this variable
print(x)
y = thisdict.keys()
print (y)
print (thisdict) # prints both keys and values
# alt
z = thisdict.items()
print(z)

# loop through the print for more readability
for i in thisdict:
    print(i)
# whole thing - keys and values

for i in thisdict:
    print(thisdict[i]) # print values only

#dictionary values can be COMPLEX data types

dict1 = {1:"Bob",2:"Ed",3:"Tony"}
dict2 = {
    1:["Bob", 34, "Student"], # dict with lists
    2:{{1: 'you', 2: 'can',3:"nest"}, # dict with dict
    3:["Tony", [ True,"single"],"Plumber"]
         }

# dictionary as a scorecard

competitors = {"Bob": 0, "Ed": [0,0,0], "Tony": 0}
#**********************************
# update a value
# dictname   key   new value
competitors["Bob"] = 5
competitors["Ed"] = [10,5,0] # 

print(competitors)
    
#****************
# adding a new key/value pair
# only append to the end of the dictinoar

competitors["Barry"] = 66

# delete from anywhere in the dictionary
# removes the key AND the value
competitors.pop("Ed")
# remove from end of dictionary
competitors.popitem()

print(competitors)

#make a menu with 2 options
# make each of those options run a function
# function 1 - add competitors
# function 2 - add score to competitor
# each of the functions should access
# your competitors dictionary and alter it
#test your program by adding a new competitor and changing a score




    





































