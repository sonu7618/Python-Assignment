"""Write a Python program that prompts the user to enter a number. 
The program should determine whether the number is prime or not. 
If the number is prime, print "The number is prime." Otherwise, print
 "The number is not prime." Continue prompting the user until they enter "exit." """

while True:
    user_input= input("Enter a number (or type 'exit' if you want to stop):").lower()
    if user_input=="exit":
        print("GoodBye!")
        break
    number=int(user_input)
    if number > 1:
        i = 2
        while i < number:
            if number % i == 0:
                print(f"{number} is not a prime number.")
                break
            i += 1
        else:
            print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
