#======================================================================================================================================
#Python Dictionaries
#======================================================================================================================================

# dictionary - data structures composed of keys and values
# they are ORDERED - the order in which the data is held cannot change
# once you set the keys you cant change them

thisDict = {"Bob": 46, "Ed": 15, "Sue": 55}
# make a dictionary using curly brackets
# keys can be any simple data types string, int, float, True
# Values can be any data type


# output data

x = thisDict.values()# print values
y = thisDict.keys() # print keys
z = thisDict.items()# print keys and values

print(x)
print(y)
print(z)

for name,value in thisDict.items():
    print(name,value)

thisDict = {"Bob": 46, "Ed": 15, "Sue": 55      }

#update value
thisDict["Bob"] = 66 # updates the value

thisDict["Barry"] = 6 # add new value

thisDict.pop("Ed")  # Deletes from anywhere in the dictionary

thisDict.popitem()  # Deletes from end of the dictionary

print(thisDict)

