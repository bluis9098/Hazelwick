table=int(input("Enter a times table between 1 and 12 plis:"))

while table < 1 or table > 12:
    table=int(input("Enter a times table between 1 and 12 plis again:"))

for i in range(1,13):
    print(table,"x",i,"=",table*i) #outputs 12 times