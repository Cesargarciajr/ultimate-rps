#importing library for random methods
import random


def get_user_input():
    """
    Function to get user input and transform the input into one of the valid options
    if not valid will print an error and restart the function
    """
    while True:
        user = input("\nSelect (R) for Rock, (P) for Paper or (S) for Scissors: ")
        if user == "r" or user == "R":
            user = "rock"
            break
        elif user == "p" or user == "P":
            user = "paper"
            break
        elif user == "s" or user == "S":
            user = "scissors"
            break
        else:
            print("\nERROR! Please select one of the valid options.")
    print(f'You choose: {user}')
    return user

def get_computer_choice():
    """
    Function to randomly gerenate between computer choice
    """
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    print(f'Computer choose: {computer}')
    return computer

def result(user, computer):
    if user == computer:
        print("its a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You Lose!")
    
def main():
    print("\nWelcome to THE ULTIMATE RPS Game!")
    print("""
        _______             ______                 _______
    ---'   ____)        ---'  ____)____        ---'   ____)____
          (_____)                ______)                 ______)
          (_____)                _______)            __________)
          (____)                _______)             (____)
    ---.__(___)         ---.__________)        ---.__(___)
        """)
    user_choice = get_user_input()
    computer_choice = get_computer_choice()
    result(user_choice, computer_choice)

main()