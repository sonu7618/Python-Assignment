"""Write a Python program that simulates a basic arithmetic quiz. 
Generate two random numbers between 1 and 30 and ask the user to 
provide the result of their multiplication. If the answer is correct, 
print "Correct!" and generate a new question. If the answer is wrong, 
print "Incorrect, try again." Allow the user to stop the quiz when the 
user enters "exit" """

import random
while True:
    first_num=random.randint(1,30)
    second_num=random.randint(1,30)
    print(f'Multiplication of {first_num} and {second_num} is:')
    user_input=input("Guess the output (or type 'exit' to quit quiz):").lower()
    if user_input=="exit":
        print("Thanks for playing!")
        break
    if user_input.isdigit():
        if first_num*second_num==int(user_input):
            print("Correct")
        else:
            print("Incorrect try again")
    else:
        print("Invalid input.Please enter number or type exit.")    