nitrate = input("Enter nitarte level 1 - 50")
if nitrate >= "10" and nitrate <= "50":
    print("Dose 3ml")
elif nitrate >= "2.5" and nitrate < "10":
    print("Dose 2ml")
elif nitrate > "1" and nitrate < "2.5":
    print("Dose 1ml")
elif nitrate > "50":
    print("enter correct level 1 - 50")
else:
    print("Dose 0.5ml")
          
