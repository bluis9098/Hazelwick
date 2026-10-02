names = ["Tanmay","Calvin","Rehaan", "Asim","Sofia","Maxwell","Isabella","Rushki","Yashvi","Swasti"]
flag = ""
ind = 0
name = input("Enter your name:")

for i in range(len(names)):
    if name == names[i]:
        ind = i
        flag = "found"

if flag == "found":
    print("Name is found at",ind+1,"position")
else:
    print("Not found")


