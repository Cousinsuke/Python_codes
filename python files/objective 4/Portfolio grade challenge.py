marks = input("Enter marks for analysis")
marks2 = input("Enter marks for design")
marks3 = input("Enter marks for implementation")
marks4 = input("Enter marks for evaluation")
total = marks + marks2 + marks3 + marks4



if total == "0" and total < "4":
    print (total)
elif total >= "4" and total < "13":
    print (total)
elif total >= "13" and total < "22":
    print (total)
elif total >= "22" and total < "31":
    print (total)
elif total >= "31" and total < "41":
    print (total)
elif total >= "41" and total < "54":
    print (total)
elif total >= "54" and total < "67":
    print (total)
elif total >= "67" and total < "80":
    print (total)
else:
    print (total)
