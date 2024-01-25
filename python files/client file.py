#TASK - create file called clients.
#       take 3 pieces of info from user
#       name, age, occupation
#       APPEND that info to the file - on a single line separated by commas
#       loop your program to APPEND 5 client details
#       print out the client details
thefile = open("Clients.txt", "w")
thefile.close()
for 1 in range (5):
    name = input("Enter your name")
    age = input("Enter your age")
    occu = input("Enter your occupation")
        
with open("Clients.txt","a") as Clients:
    thefile.write(name)
    thefile.write(",")
    thefile.write(age)
    thefile.write(",")
    thefile.write(occu)
    
with open("Clients.txt","r") as Clients:
    for line in Clients:
        print(line.strip("\n"))

for 1 in range (5):
    with open("Clients.txt","a") as thefile:
        thefile.write(input("enter your name:"))
    


    
