#importing library for random methods
import random
user_score = 0
computer_score = 0

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
        elif user == "gun" or user == "Gun" or user == "GUN" or user == "g" or user == "G":
            print(f'''\n You have typed "{user}" and unlocked the Gun. You're the RPS MASTER! YOU WON!!!
                        ︵  
                       |  |
                    ---'  '________
                           _________)
                          (_____)
                          (____)
                    ---.__(___)''')
            user = "gun"
            break
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
        print("""\nComputer chose: Rock
                  _______
                (____)   '---
               (_____)
               (_____)
                (____)
                 (___)__.---""")
    elif computer == "paper":
        print("""\nComputer chose: Paper
                  ______
             ___(____   '---
           (______
          (_______
           (_______
             (__________.---""")
    else:
        print("""\nComputer chose: Scissors
                 ______
             __(____   '---
           (______
          (_________
               (____)
                (___)__.---""") 

    return computer

def result(user, computer):
    global user_score
    global computer_score
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
        user_score = user_score + 1
    elif user == "paper" and computer == "rock":
        print("""\nYou Won this Round!
                  ︵  
                 |  |
              ---'  '_____
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
        user_score = user_score + 1
    elif user == "scissors" and computer == "paper":
        print("""\nYou Won this Round!
                  ︵  
                 |  |
              ---'  '_____
                    (_____)
                    (_____)
                    (____)
              ---.__(___)""")
        user_score = user_score + 1
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
        computer_score = computer_score + 1  
    return result
    
def main():
    global user_score
    global computer_score
    print("""\n                  Welcome to THE ULTIMATE RPS Game!
             \n     Challenge the computer for a 5 round game and see if you can beat it.
             \r                  Win 3 times in a row to unlock secret!")
             \n                         Good Luck and have fun!""")
    print("""
        _______             ______                 _______
    ---'   ____)        ---'  ____)____        ---'   ____)____
          (_____)                ______)                 ______)
          (_____)                _______)            __________)
          (____)                _______)             (____)
    ---.__(___)         ---.__________)        ---.__(___)
        """)
    round = 1
    while round <=5:
        print(f'''
 ------------------------------------------------------------------------------
|                                 ROUND: {round}                                     |
 ------------------------------------------------------------------------------
|                               User: {user_score} | Computer: {computer_score}                          |
 ------------------------------------------------------------------------------''')
        user_choice = get_user_input()
        if user_choice == "gun":
            print("""
         __                                _                  
        |  |                              | |                 
        |  |      ___  __ _  ___ _ __   __| |
        |  |     / _ \/ _` |/ _ \ '_ \ / _` |
        |  |____|  __/ (_| |  __/ | | | (_| |
        |_______|\___|\__, |\___|_| |_|\__,_|
                       __/ |
                      |___/""")
            break
        else:
            computer_choice = get_computer_choice()
            result(user_choice, computer_choice)
        round = round + 1

main()