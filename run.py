#importing library for random methods
import random


def get_user_input():
    """
    Function to get user input and transform the input into one of the valid options
    if not valid will print an error and restart the function
    """
    while True:
        user = input("\nSelect (R) for rock, (P) for Paper or (S) for Scissors: ")
        if user == "r" or user == "R":
            user = "rock"
            get_computer_choice()
            break
        elif user == "p" or user == "P":
            user = "paper"
            get_computer_choice()
            break
        elif user == "s" or user == "S":
            user = "scissors"
            get_computer_choice()
            break
        else:
            print("\nError! Please select one of the valid options.")

def get_computer_choice():
    """
    Function to randomly choose between options and play as computer
    """
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    print(computer)

get_user_input()
