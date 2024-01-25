
with open("results.txt","a") as theFile: #open as apend will create the file
    for i in range(6): #for loop to stop at the 6
        name = input("Enter name:")
        score = input("Enter score out of 100:")
        theFile.write (name+","+score+"\n") 


