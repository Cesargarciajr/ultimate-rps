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
            rock_fig = print(""" \nYou chose: Rock
                  _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
            break
        elif user == "p" or user == "P":
            user = "paper"
            paper_fig = print(""" \nYou chose: Paper
                  ________
              ---'    ____)____
                         ______)
                        _______)
                       _______)
              ---.__________)""")
            break
        elif user == "s" or user == "S":
            user = "scissors"
            scissors_fig = print(""" \nYou chose: Scissors
                  _______
              ---'   ____)____
                        ______)
                    __________)
                    (____)
              ---.__(___) """)
            break
        elif user == "gun" or user == "Gun" or user == "g":
            user = "gun"
            print("""\nYou have unlocked the Gun. You're the RPS MASTER!
                  ︵  
                 |  |
              ---'  '__________
                     __________)
                    (_____)
                    (____)
              ---.__(___)""")
        else:
            print("\nERROR! Please select one of the valid options.")
    return user

def get_computer_choice():
    """
    Function to randomly gerenate between computer choice
    """
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    if computer == "rock":
        print("""\nComputer chose: Rock!
                 ________
                (____)   '---
               (_____)
               (_____)
                (____)
                 (___)__.---""")
    elif computer == "paper":
        print("""\nComputer chose: Paper!
                 _______
            ____(____   '---
           (______
          (_______
          (_______
             (__________.---""")
    else:
        print("""\nComputer chose: Scissors!
                _______
           ____(____   '---
          (______
          (__________
               (____)
                (___)__.---""") 

    return computer

def result(user, computer):
    if user == computer:
        print("""\nIts a tie!
                    __
                   /  \ 
                   \__/
                   /  \ 
                  /    \ 
                  \    /
                   \  /
                    \/""")
    elif user == "rock" and computer == "scissors":
        print("""\nYou Won this Round!
                  ︵  
                 |  |
              ---'  '_____
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
    elif user == "paper" and computer == "rock":
        print("""\nYou Won this Round!
                  ︵  
                 |  |
              ---'  '_____
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
    elif user == "scissors" and computer == "paper":
        print("""\nYou Won this Round!
                  ︵  
                 |  |
              ---'  '_____
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
    elif user == "gun":
            print()
    else:
                print("""\nYou Lose!
             _________
            (____)    '---
            (_____)
            (_____)
             (____) __.---
                '  '
                |  |
                 ︶        """)
    
def main():
    print("""\n                     Welcome to THE ULTIMATE RPS Game!
             \nChallenge the computer for a 5 round game and see if you can beat the Computer BEAST.
                Win 3 times in a row to unlock secret!")
             \n                         Good Luck and have fun!""")
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