"""Create a Python program that prompts the user to enter their age. 
If the age is less than 18, print "You are a minor." If the age is 
between 18 and 60, print "You are an adult." For ages over 60, print 
"You are a senior citizen." The program should continue until the user 
inputs "stop." """

while True:
    user_input=input("Enter your age (or type stop if you want to end):")
    if user_input=="stop":
        break
    age=int(user_input)
    if age<18:
        print("You are minor.")
    elif 18<=age <=60:
        print("You are adult.")
    else:
        print("You are senior citizen.")