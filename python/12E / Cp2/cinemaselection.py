age = int(input("Enter your age:"))


if age < 12:
    print("5")
elif age >= 12 and age <=17:
    print("7")
elif age>=18 and age <=64:
    sc = input("Enter y for yes and n for no:")
    if sc == "y":
        print("8")
    else:
        print("10")
elif age > 65:
    print("6")
else:
    print("invalid")