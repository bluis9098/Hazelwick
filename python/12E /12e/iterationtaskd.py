import random
number = random.randint(1,100)
count = 1
guess = int(input("Enter your guess:"))

while guess != number:
    count = count+1
    if guess > number:
        print("Too high")
    else:
        print("Too Low")
    guess = int(input("Enter your guess:"))

print("You got it right in",count,"times!")

