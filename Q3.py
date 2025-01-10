""" Write a Python program that continuously prompts the user 
to input a fruit name. If the input is "apple," the program 
should print "You got it!" and stop. Otherwise, it should 
display "Try again" and continue."""

while True:
    user_input=input("Enter a fruit name:").lower()
    if user_input!="apple":
        print("Try again.")
    else:
        print("You got it.")
        break