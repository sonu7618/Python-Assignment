""" Write a Python program that generates a random number 
between 1 and 10 and prompts the user to guess the number. 
The program should provide hints such as "guess higher" or 
"guess lower" based on the user's input. Once the user guesses
the correct number, the program should display the number of 
attempts it took to guess the correct number."""

import random
random_num=random.randint(1,10)
attempts=0
while True:
    attempts+=1
    user_input=int(input("Guess the number between 1 to 10:"))
    if user_input>random_num:
        print("Guess lower.")
    elif user_input<random_num:
        print("Guess higher.")
    else:
        print(f"Congratulation! You have successfully guessed the correct number {random_num} in {attempts} attempts.")
        break