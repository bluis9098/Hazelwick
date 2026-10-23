A = 0
B = 0
C = 0
total=0
vote = ""

while vote!="End":
    vote=input("Enter your Vote")
    if vote == "A":
        A=A+1
    elif vote =="B":
        B=B+1
    elif vote == "C":
        C=C+1

total = A+B+C
print("A:",A)
print("B",B)
print("C",C)
print("Total:",total)