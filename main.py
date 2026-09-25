# Guess Number Game

import random

print("....Welcome to Guess Game....\n")

computer_no = random.randint(1,10)
user_attempt = 0

while(True):
    user_no = int(input("Guess the number: "))
    user_attempt += 1
    
    if (user_no == computer_no):
        print(f"\nHurray ! Your Guess is Correct...")
        break
    elif (user_no > computer_no):
        print("Your guess is higher than number !!")
    elif (user_no < computer_no):
        print("Your guess is lower than number !!")
    else:
        print("Invalid no. submit by You, Try Again !!")
        
total_attempt = user_attempt
print(f"You guess the correct number in {user_attempt} attempts...")

