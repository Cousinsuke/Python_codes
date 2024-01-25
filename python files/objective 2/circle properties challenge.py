num = int(input("enter circle diameter"))
total = num / 2 #radius
print ("the radius is")
print (round(total))

total2 = (total * total) * 3.14 #area
print ("the area is")
print (round(total2))

total3 = num * 3.14 #circumference
print ("the cirumference is")
print (round(total3))

num2 = int(input("enter circle arc angle"))
total4 = (total3 * num2) / 360 #arc length
print ("the arc lenght is")
print (round(total4))
