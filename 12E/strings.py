fname = input("Enter your first name:")
lname = input("Enter your last name:")

initial = fname[0]
part2 = lname[0:4]
length = len(fname) + len(lname)

username = (initial + part2 + str(length)).lower()

print("The username is:",username))
