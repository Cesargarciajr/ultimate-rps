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
            print(f'user choice: {user}')
            get_computer_choice()
            break
        elif user == "p" or user == "P":
            user = "paper"
            print(f'user choice: {user}')
            get_computer_choice()
            break
        elif user == "s" or user == "S":
            user = "scissors"
            print(f'user choice: {user}')
            get_computer_choice()
            break
        else:
            print("\nError! Please select one of the valid options.")

def get_computer_choice():
    """
    Function to randomly gerenate between computer choice
    """

    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    print(f'computer choice: {computer}')
    result(computer, user)

def result(user, computer):
    """
    Function to compare the choices, print the result and count the rounds
    """
    round = 0
    while round <= 5 :
        if user == computer:
            print("its a tie!Let's try again")
            round +1
            get_user_input()
        elif user == "rock" and computer == "scissors":
            print("You win!")
            round +1
        elif user == "paper" and computer == "rock":
            print("You win!")
            round +1
        elif user == "scissors" and computer == "paper":
            print("You win!")
            round +1
        else:
            print("You Lose!")
            round +1

