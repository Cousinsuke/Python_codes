#using external files in python
# we can READ, WRITE, or APPEND to an external file in python

#create and open an external file

thefile = open("thefile.txt", "w") #w means write
thefile.write ("This will also write to the file\n") #write to the .txt file

#write is DESTRUCTIVE - it will overwrite each time
thefile.write("is this on the same line or another line?\n")
thefile.write("another line of text\n")

thefile.write("bob")
thefile.write(",")
thefile.write("35")
thefile.write(",")
thefile.write("Builder\n")

thefile.close()

#           csv - comma separated values
thefile = open("thefile.csv", "w") #w means write
thefile.write ("This will also write to the file\n") #write to the .csv file

thefile.close()


#we often use APPEND mode to add things to files we have created
thefile = open("thefile.txt", "a") # a means append
thefile.write ("This will append to the file\n")

thefile.close()

with open("thefile.txt","a") as thefile:
    thefile.write("open and close automatically\n")
# it auto closes the line

with open("thefile.txt","r") as thefile: # r means read
    for line in thefile:
        print(line.strip("\n"))
    


