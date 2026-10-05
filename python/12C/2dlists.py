names = ["Oliver","Adrian","Leon"]

scores = [[65,72,58,80],[90,85,88,92],[45,60,52,49]]


for row in range(len(scores)):
    total = 0
    for col in range(len(scores[row])):
        total = total + scores[row][col]
    average = total/len(scores[row])
    print(names[row],":","Total is",total,"Average is:", average)

for col in range(len(scores[0])):
    total = 0
    for row in range(len(scores)):
        total = total + scores[row][col]
    print("The average for test",col+1,":",total/len(scores))