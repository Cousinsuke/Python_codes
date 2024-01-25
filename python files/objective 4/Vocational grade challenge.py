marks = input("Marks out of 100")
if marks < "40":
    print("FAIL!")
elif marks >= "40" and marks < "60":
    print("PASS!")
elif marks >= "60" and marks < "80":
    print("MERIT!")
else:
    print("DISTINCTION!")
