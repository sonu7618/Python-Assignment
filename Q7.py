"""Write a Python program that simulates a login system. The program 
should prompt the user to enter a username and password. If both are 
correct (e.g., username is "admin" and password is "1234"), 
print "Login successful" and exit. If either is incorrect, 
print "Invalid credentials, try again." Allow the user up to 
3 attempts before locking them out with the message "Too many failed attempts." """

attempts=0
while True:
    user_name=input("Enter your username:")
    password=input("Enter your password:")
    if user_name!="admin" and password!="1234":
        attempts+=1
        print("Invalid credentials")
        if attempts==3:
            print("Too many failed attempts.You are locked out.")
            break
    else:
        print("Login successful.")
        break