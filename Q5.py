"""Write a Python program that keeps asking the user to enter a 
day of the week. If the input is not "Sunday," print "It's not 
the weekend yet." The loop should break and print "Enjoy your weekend!"
 when the input is "Sunday." """

while True:
    user_input=input("Enter the day of week:").lower()
    if user_input!="sunday":
        print("It's not the weekend yet.")
    else:
        print("Enjoy your weekend!")
        break