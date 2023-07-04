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
        elif user == "p" or user =="P":
            user = "paper"
        elif user == "s" or user == "S":
            user = "scissors"
        else:
            print("\nError! Please select one of the valid options.")
    
get_user_input()