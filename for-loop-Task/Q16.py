# Python program to check the validity of username and password input by users

for i in range(3,0,-1):
    user_name=input("Enter vaild user name:")
    password=input("Enter vaild password:")
    if user_name!="sonu" or password!="4567":
        if i==1:
            continue
        print("Invaild username or password.","please type vaild username or password")
    else:
        print("Logged in succesfully")
        break
else:
    print("You are blocked")