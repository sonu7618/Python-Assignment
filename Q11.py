"""Write a Python program that prompts the user to repeatedly enter a name. 
If the user enters the phrase "good luck," the program keeps track of how many 
times the phrase has been entered. When the phrase has been entered three times, 
the program should display a message stating "You typed good luck three times." 
For each entry of "good luck" before the third occurrence, display the message 
"You typed the same word [count] times." Continue this process until the phrase 
has been entered three times."""

count=0
while True:
    user_input=input("Enter a name or phrase:").lower()
    if user_input=="good luck":
        count+=1
        if count<3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times")
            break