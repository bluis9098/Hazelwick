mark = int(input("Enter your mark:"))

#printing error message
if mark < 0 or mark > 100:
    print("Try again and enter a valid value!")
elif mark > 70:
    print("A")
elif mark > 60:
    print("B")
elif mark > 50:
    print("C")
elif mark > 40:
    print("D")
else:
    print("U")


