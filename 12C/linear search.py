names=["Leon","Oliver","Raahil","Dhyan","Alfie","Hassan","Afqi","Yog","Yug"]

answers = input("Enter your name:")

found = False
index =0

for i in range(len(names)):
    if names[i] == answers:
        index = i
        found = True
        break


if found:
    print(answers, " is in the list at",index, "position")
else:
    print("It is not in.")