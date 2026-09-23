grade=int(input("Enter your grade:"))

if grade < 0 or grade > 100:
    print("ERROR")
elif grade > 70:
    print("A")
elif grade > 60:
    print("B")
elif grade > 50:
    print("C")
elif grade > 40:
    print("D")
else:
    print("U")
