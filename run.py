# Importing libraries from random, time effect/delay an for clear the screen
import random
import time
import os

# Defining global variables that counts the scores
user_score = 0
computer_score = 0


def get_user_input():
    """
    Function to get user input and transform the input into one of the valid
    options if not valid will print an error and restart the function
    """
    # Loop will get user input validate and store in the variable
    while True:
        user = input("\nSelect (R) Rock, (P) Paper or (S) Scissors:")
        if user == "r" or user == "R":
            user = "rock"
            break
        elif user == "p" or user == "P":
            user = "paper"
            break
        elif user == "s" or user == "S":
            user = "scissors"
            break
        elif user == "gun" or user == "GUN" or user == "g" or user == "G":
            os.system("clear")
            print(f'''\n         You have typed "{user}" and unlocked the Gun.
            You're the RPS MASTER! YOU WON!!!
                        ︵
                       |  |
                    ---'  '_______
                           ________)
                          (_____)
                          (____)
                    ---.__(___)''')
            user = "gun"
            break
        else:
            # If user input is invalid this message will be printed 
            print("\nInvalid choice. Please select one of the options!")
    return user


def get_computer_choice():
    """
    Function to randomly gerenate between computer choice
    """
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    return computer


def result(user, computer):
    """
    Function to compare results and print out the outcome
    also count the scores
    """
    # Setting the global variables to the local scope
    global user_score
    global computer_score
    # Start the contitionals to check the user input and computer choice
    if user == computer:
        os.system("clear")
        print("""\n                                    Its a tie!
                                        __
                                       /  \ 
                                       \__/
                                       /  \ 
                                      /    \ 
                                      \    /
                                       \  /
                                        \/""")
    elif user == "rock" and computer == "scissors":
        os.system("clear")
        print(""" 
    \n               You chose: Rock           Computer chose: Scissors
                        _______                      ______
                    ---'   ____)                 __(____   '---
                          (_____)              (______
                          (_____)             (_________
                          (____)                   (____)
                    ---.__(___)                     (___)__.---""")
        print("""\n                                You Won this Round!
                                        ︵
                                       |  |
                                    ---'  '_____
                                          (_____)
                                          (_____)
                                          (____)
                                    ---.__(___)""")
        user_score = user_score + 1
    elif user == "paper" and computer == "rock":
        os.system("clear")
        print(""" 
    \n                You chose: Paper          Computer chose: Rock
                    ________                       _______
                ---'    ____)____                (_____   '---
                            ______)              (_____)
                            _______)             (_____)
                           _______)               (____)
                ---.__________)                    (___)__.---""")
        print("""\n                                You Won this Round!
                                        ︵
                                       |  |
                                    ---'  '_____
                                          (_____)
                                          (_____)
                                          (____)
                                    ---.__(___)""")
        user_score = user_score + 1
    elif user == "scissors" and computer == "paper":
        os.system("clear")
        print("""
    \n                You chose: Scissors       Computer chose: Paper
                    _______                       ______
                ---'   ____)____             ___(____   '---
                           ______)         (______
                       __________)        (_______
                      (____)               (_______
                ---.__(___)                  (__________.---""")
        print("""\n                                You Won this Round!
                                        ︵
                                       |  |
                                    ---'  '_____
                                          (_____)
                                          (_____)
                                          (____)
                                    ---.__(___)""")
        user_score = user_score + 1
    elif user == "scissors" and computer == "rock":
        os.system("clear")
        print("""
    \n               You chose: Scissors       Computer chose: Rock
                    _______                        ______
                ---'   ____)____                 (_____  '---
                           ______)              (_____)
                       __________)              (_____)
                      (____)                     (____)
                ---.__(___)                       (___)__.---""")
        print("""\n                               You Lose this Round!
                                    _______
                                  (____)   '---
                                 (_____)
                                 (_____)
                                  (____).  .---
                                        |  |
                                         ︶""")
        computer_score = computer_score + 1
    elif user == "paper" and computer == "scissors":
        os.system("clear")
        print("""
    \n               You chose: Paper          Computer chose: Scissors
                    ________                        ______
                ---'    ____)____              ___(____   '---
                            ______)          (________
                            _______)         (_________
                           _______)               (____)
                ---.__________)                    (___)__.---""")
        print("""\n                               You Lose this Round!
                                    _______
                                  (____)   '---
                                 (_____)
                                 (_____)
                                  (____).  .---
                                        |  |
                                         ︶""")
        computer_score = computer_score + 1
    elif user == "rock" and computer == "paper":
        os.system("clear")
        print("""
    \n              You chose: Rock           Computer chose: Paper
                        _______                      ______
                    ---'   ____)                 __(____   '---
                          (_____)              (______
                          (_____)             (_______
                          (____)               (_______
                    ---.__(___)                    (_______.---""")
        print("""\n                               You Lose this Round!
                                    _______
                                  (____)   '---
                                 (_____)
                                 (_____)
                                  (____).  .---
                                        |  |
                                         ︶""")
        computer_score = computer_score + 1
    return result


def winner(rounds):
    """
    This function will compare the final scores and print the final message
    if user wins, lose or a tie
    """
    # Defining global variables in the local scope
    global user_score
    global computer_score
    # Conditional checking rounds and nested conditional to check the scores
    if rounds >= 5:
        if user_score > computer_score:
            os.system("clear")
            print(f'''\n
    ---------------------------------------------------------------------------
    |                    You scored: {user_score} | Computer Scored: {computer_score}                    |
    ---------------------------------------------------------------------------                            
                                CONGATULATIONS YOU WON THE GAME!!!
                                        .-=========-.
                                         \-=======-/
                                        _|         |_
            You Scored: {user_score}              ((|   .=.   |))
            Computer Scored: {computer_score}          \|   /|\   |/
                                         \__ '`' __/
                                           _`) (´_
                                         _/_______\_
                                       _/___________\_''')
            return_main()
        elif user_score < computer_score:
            os.system("clear")
            print(f'''\n
    ---------------------------------------------------------------------------
    |                    You scored: {user_score} | Computer Scored: {computer_score}                    |
    ---------------------------------------------------------------------------
                             ____
                            / ___| __ _ _ __ ___   ___
                           | |  _ / _` | '_ ` _ \ / _ \ 
                           | |_| | (_| | | | | | |  __/
                            \____|\__,_|_| |_| |_|\___|
                                 ___
                                / _ \__   _____ _ __
                               | | | \ \ / / _ \ '__|
                               | |_| |\ V /  __/ |
                                \___/  \_/ \___|_|''')
            return_main()
        else:
            os.system("clear")
            print(f'''
 ------------------------------------------------------------------------------
|                    You scored: {user_score} | Computer Scored: {computer_score}                       |
 ------------------------------------------------------------------------------
                        ___ _
                       |_ _| |_ ___       __ _
                        | || __/ __|     / _` |
                        | || |_\__ \    | (_| |
                       |___|\__|___/     \__,_|
                               _____ _
                              |_   _(_) ___
                                | | | |/ _ \ 
                                | | | |  __/
                                |_| |_|\___|''')
            return_main()


def return_main():
    """
    Return to main menu option through user input.
    """
    # Loop will validate the user input or print invalid option
    while True:
        print("\n")
        choice = input(
'\nClick the "RUN PROGRAM" button to restart the program or to Main Menu, press (M): ')
        if choice == 'M' or choice == 'm':
            menu()
            break
        else:
            print("Invalid input, please try again.")
            continue


def start_game():
    """
    Function to start the game and control the game flow
    """
    # Defining the global variables to local scope
    global user_score
    global computer_score
    os.system('clear')
    print("""
                _______             ______                 _______
            ---'   ____)        ---'  ____)____        ---'   ____)____
                  (_____)                ______)                 ______)
                  (_____)                _______)             _________)
                  (____)                _______)             (____)
            ---.__(___)         ---.__________)        ---.__(___)""")
    # Sets first round and start a loop that counts the rounds
    round = 1
    while round <= 5:
        print(f'''
 -----------------------------------------------------------------------
|                               ROUND: {round}                                |
 -----------------------------------------------------------------------
|                           You: {user_score} | Computer: {computer_score}                        |
 -----------------------------------------------------------------------''')
        # call the function to get user input and checks if user chose gun to break the loop
        user_choice = get_user_input()
        if user_choice != "gun":
            # If gun is not selected then will call computer, results and winner functions
            # until round is reached to 5 so the loop stops
            computer_choice = get_computer_choice()
            result(user_choice, computer_choice)
            winner(round)
        else:
            print("""
         __                                _
        |  |                              | |
        |  |      ___  __ _  ___ _ __   __| |
        |  |     / _ \/ _` |/ _ \ '_ \ / _` |
        |  |____|  __/ (_| |  __/ | | | (_| |
        |_______|\___|\__, |\___|_| |_|\__,_|
                       __/ |
                      |___/""")
            return_main()
            break
        # Round counter
        round = round + 1


def menu():
    """
    Menu functions the will print options for the user
    """
    os.system("clear")
    # Loop will validate input and print options to the user
    while True:
            print("""\n               --------------------- MENU --------------------------
                    \r              |                                                     |
                    \r              |    Please select one of the following, options:     |
                    \r              |                                                     |
                    \r              | - Press (S) to Start the Game                       |
                    \r              | - Press (R) to see the Rules of the Game            |
                    \r              | - Press (C) for credits                             |
                    \r              |_____________________________________________________|""")
            menu_selection = input("\n              Please select an option: ")
            # Conditionals to check user input and redirect to respective menu options
            if menu_selection == "S" or menu_selection == "s":
                start_game()
            elif menu_selection == "R" or menu_selection == "r":
                os.system('clear')
                print("""\n                 --------------------- HOW TO PLAY -----------------------
            \n            • Game has 5 Rounds
            • Each round you can choose from Rock, Paper or Scissors options
            • Once you have selected one of the options the computer will play
            • Results will be printed at the screen if you win or lose that round or even a tie
            • A score counter will count the points
            • After the 5th round will be displayed the Winner or Loser of the game
            • Just keep in mind that:
                - Rock beats Scissors
                - Papers beats Rock
                - Scissors beats Paper
            • You might unlock the Fatality mode if you win 3 times in a row
            • Pay attention to the hints to unluck the MASTER RPS and become a Legend
            • Have Fun!""")
                return_main()
            elif menu_selection == "c" or menu_selection == "C":
                os.system("clear")
                print("""
            \n                    This Game was Developed by
            \n                          Cesar Garcia
            \n                      github.com/Cesargarciajr
            \r              linkedin.com/in/cesar-garcia-637973aa""")
                return_main()
            else:
                print("Invalid input, please try again.")
                continue

def main():
    """
    Main function control the game flow and call the functions
    and start the game
    """
    print("""
    \n                 Welcome to THE ULTIMATE RPS Game!
    \n    Challenge the computer for a 5 round game and see if you can beat it.
    \r               Win 3 times in a row to unlock secret!
    \n                      Good Luck and have fun!""")
    print("""
                _______             ______                 _______
            ---'   ____)        ---'  ____)____        ---'   ____)____
                  (_____)                ______)                 ______)
                  (_____)                _______)             _________)
                  (____)                _______)             (____)
            ---.__(___)         ---.__________)        ---.__(___)
        """)
    # Gives 4.5 second fo the user to read intro message
    print('Loading...')
    time.sleep(4.5)
    print('Completed')
    os.system("clear")
    menu()

# Calling function to Start the Program
main()
