height= float(input("Enter your height:"))
adult = input("Enter Y if you are with an adult otherwise enter N:")

if height >= 140:
    print("Allowed")
elif height >=120 and adult =="y":
    print("Allowed")
else:
    print("Not allowed!")