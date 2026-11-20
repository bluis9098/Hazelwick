riders = 0

while riders <= 8:
    height = int(input("Enter your height:"))
    if height < 140 and height >= 120:
        q = input("Are you riding with an adult:")
        if q == "yes":
            print("You are allowed to ride with an adult!")
            rider = rider+1
        else:
            print("You are not allowed!")
    elif height >= 140:
        print("You are allowed to ride!")
        rider= rider+1
    else:
        print("You are not allowed to ride")

print("Ride is full now! Come back Later")
