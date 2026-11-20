table=int(input("Which times table do you want enter between 1 and 12 only plis:"))
while table < 1 or table > 12:
    table=int(input("Which times table do you want enter between 1 and 12 only plis again:"))

for i in range(1,13):
    print(table,"x",i,"=",i*table)