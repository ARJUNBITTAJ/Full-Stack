credential = "0312"

while True:
    password = int(input("enter the password:"))

    if credential == password:
        print("login success")
        break;
    else:
        print("incorrect password")


