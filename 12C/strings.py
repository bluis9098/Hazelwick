fname=input("Enter your first name:")
lname=input("Enter your second name:")

initial=fname[0]
part2 = lname[0:4]
length = len(fname) + len(lname)

username = (initial + part2 + str(length)).lower()

print("Username is:",username)