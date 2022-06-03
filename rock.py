import random

possible_entries = ["R","S","P"]

user_entry = input("Please choose between R for Rock, P for Paper, S for Scissors:").upper()

a = 0

while a == 0:
    computer_entry = random.choice(possible_entries)
    print("Player(" + user_entry + ") : CPU("+computer_entry+")")

    if user_entry not in possible_entries:
        print("Invalid Entry")
        user_entry = input("Please choose between R for Rock, P for Paper, S for Scissors:").upper()
    else:
        if user_entry == computer_entry:
            print("Its a tie")
            user_entry = input("Please choose between R for Rock, P for Paper, S for Scissors:").upper()
        elif user_entry == "R" and computer_entry == "P":
            print("Computer Wins")
            a = 1
        elif user_entry == "S" and computer_entry == "P":
            print("You Win")
            a = 1
        elif user_entry == "P" and computer_entry == "S":
            print("Computer Wins")
            a = 1
        elif user_entry == "P" and computer_entry == "R":
            print("You Win")
            a = 1
        elif user_entry == "R" and computer_entry == "S":
            print("You Win")
            a = 1
        elif user_entry == "S" and computer_entry == "R":
            print("Computer Wins")
            a = 1