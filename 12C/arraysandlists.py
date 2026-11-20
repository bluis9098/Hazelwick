temprature =[]

for i in range(5):
    temp = float(input("Enter the temprature:"))
    temprature.append(temp)

highest = temprature[0]
total =0

for t in temprature:
    total = total + t
    if t > highest:
        highest = t

average = total / len(temprature)
above = 0
for te in temprature:
    if te > average:
        above = above + 1

print("The tempratures are:",temprature)
print("The average is:",average)
print("The highest is:",highest)
print("There are",above,"Temperatures above average")

