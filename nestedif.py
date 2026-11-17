while True:
    username=input("Enter your username:")

    if username == "admin":
        password = input("Enter your password:")
        if password == "Secret1":
            print("Access Granted")
        else:
            print("Wrong password!")
    else:
        print("unknown User")