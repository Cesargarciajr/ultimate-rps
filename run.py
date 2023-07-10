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
        user = input("\nSelect (R) Rock, (P) Paper or (S) Scissors: ")
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
        print(f'''
        \n                      You both chose the same
        \n                            Its a tie!
        \n                                __
        \r                               /  \ 
        \r                               \__/
        \r                               /  \ 
        \r                              /    \ 
        \r                              \    /
        \r                               \  /
        \r                                \/''')
    elif user == "rock" and computer == "scissors":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r                _______                      ______
        \r            ---'   ____)                 __(____   '---
        \r                  (_____)              (______
        \r                  (_____)             (_________
        \r                  (____)                   (____)
        \r            ---.__(___)                     (___)__.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                       You Won this Round!
        \r                                ︵
        \r                               |  |
        \r                            ---'  '_____
        \r                                  (_____)
        \r                                  (_____)
        \r                                  (____)
        \r                            ---.__(___)""")
        user_score = user_score + 1
    elif user == "paper" and computer == "rock":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r                ________                       _______
        \r            ---'    ____)____                (_____   '---
        \r                        ______)             (_____)
        \r                        _______)            (_____)
        \r                       _______)              (____)
        \r            ---.__________)                   (___)__.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                       You Won this Round!
        \r                                ︵
        \r                               |  |
        \r                            ---'  '_____
        \r                                  (_____)
        \r                                  (_____)
        \r                                  (____)
        \r                            ---.__(___)""")
        user_score = user_score + 1
    elif user == "scissors" and computer == "paper":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r                _______                       ______
        \r            ---'   ____)____             ___(____   '---
        \r                       ______)         (______
        \r                    __________)        (_______
        \r                  (____)               (_______
        \r            ---.__(___)                  (__________.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                       You Won this Round!
        \r                                ︵
        \r                               |  |
        \r                            ---'  '_____
        \r                                  (_____)
        \r                                  (_____)
        \r                                  (____)
        \r                            ---.__(___)""")
        user_score = user_score + 1
    elif user == "scissors" and computer == "rock":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r               _______                        ______
        \r           ---'   ____)____                 (_____  '---
        \r                      ______)              (_____)
        \r                   __________)             (_____)
        \r                 (____)                     (____)
        \r           ---.__(___)                       (___)__.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                      You Lost this Round!
        \r                            _______
        \r                          (____)   '---
        \r                         (_____)
        \r                         (_____)
        \r                          (____).  .---
        \r                                |  |
        \r                                 ︶""")
        computer_score = computer_score + 1
    elif user == "paper" and computer == "scissors":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r                ________                        ______
        \r            ---'    ____)____              ___(____   '---
        \r                        ______)          (________
        \r                        _______)         (_________
        \r                       _______)               (____)
        \r            ---.__________)                    (___)__.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                      You Lost this Round!
        \r                            _______
        \r                          (____)   '---
        \r                         (_____)
        \r                         (_____)
        \r                          (____).  .---
        \r                                |  |
        \r                                 ︶""")
        computer_score = computer_score + 1
    elif user == "rock" and computer == "paper":
        os.system("clear")
        print(f'''
        \n        Your chose: {user}               Computer chose: {computer}
        \r                _______                      ______
        \r            ---'   ____)                 __(____   '---
        \r                  (_____)              (______
        \r                  (_____)             (_______
        \r                  (____)               (_______
        \r            ---.__(___)                    (_______.---''')
        time.sleep(1.5)
        os.system("clear")
        print("""
        \n                      You Lost this Round!
        \r                            _______
        \r                          (____)   '---
        \r                         (_____)
        \r                         (_____)
        \r                          (____).  .---
        \r                                |  |
        \r                                 ︶""")
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
    if rounds >= 5 or user_score == 3:
        if user_score == 3:
            os.system("clear")
            print("""
        \n                    You WON 3 rounds!
        \r                       FINISH HIM!
        \r                             _______
        \r           __,_____         |.-----.|
        \r          / __.==--"        ||x . x||
        \r         /#(-'              ||_.-._||
        \r         `-'                `--)-(--`
        \r                           __[=== o]___
        \r                          |:::::::::::|\ 
        \r                          `-=========-`()""")
            fatality = input("\nPress (F) for FATALITY: ")
            if fatality == "f" or fatality == "F":
                os.system("clear")
                print("""
        \n            █████▒▄▄▄     ▄▄▄█████▓ ▄▄▄       ██▓     ██▓▄▄▄█████▓▓██   ██▓  # noqa
        \r          ▓██   ▒▒████▄   ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒▓  ██▒ ▓▒ ▒██  ██▒
        \r          ▒████ ░▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██▒▒ ▓██░ ▒░  ▒██ ██░
        \r          ░▓█▒  ░░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ░██░░ ▓██▓ ░   ░ ▐██▓░
        \r          ░▒█░    ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░██████▒░██░  ▒██▒ ░   ░ ██▒▓░
        \r           ▒ ░    ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░▓    ▒ ░░      ██▒▒▒
        \r           ░       ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░    ░     ▓██ ░▒░
        \r           ░ ░     ░   ▒    ░        ░   ▒     ░ ░    ▒ ░  ░       ▒ ▒ ░░
        \r                       ░  ░              ░  ░    ░  ░ ░            ░ ░
                                                            ░ ░""")
            else:
                print('Missed')
                # Restart the score count
            user_score = 0
            computer_score = 0
            return_main()
        elif user_score > computer_score:
            os.system("clear")
            print(f'''
    \n ---------------------------------------------------------------------
    \r|                    You scored: {user_score} | Computer Scored: {computer_score}               | # noqa
    \r ---------------------------------------------------------------------
    \r                       CONGATULATIONS YOU WON THE GAME!!!
    \n                                .-=========-.
    \r                                 \-=======-/
    \r                                _|         |_
    \r                               ((|   .=.   |))
    \r                                \|   /|\   |/
    \r                                 \__ '`' __/
    \r                                   _`) (´_
    \r                                 _/_______\_
    \r                               _/___________\_''')
            # Restart the score count
            user_score = 0
            computer_score = 0
            return_main()
        elif user_score < computer_score:
            os.system("clear")
            print(f'''
    \n ---------------------------------------------------------------------
    \r|                    You scored: {user_score} | Computer Scored:{computer_score}                | # noqa
    \r ---------------------------------------------------------------------
    \n                         ____
    \r                        / ___| __ _ _ __ ___   ___
    \r                       | |  _ / _` | '_ ` _ \ / _ \ 
    \r                       | |_| | (_| | | | | | |  __/
    \r                        \____|\__,_|_| |_| |_|\___|
    \r                             ___
    \r                            / _ \__   _____ _ __
    \r                           | | | \ \ / / _ \ '__|
    \r                           | |_| |\ V /  __/ |
    \r                            \___/  \_/ \___|_|''')
            # Restart the score count
            user_score = 0
            computer_score = 0
            return_main()
        else:
            os.system("clear")
            print(f'''
    \n ---------------------------------------------------------------------
    \r|                    You scored: {user_score} | Computer Scored:{computer_score}                | # noqa
    \r ---------------------------------------------------------------------
    \n                            ___ _
    \r                           |_ _| |_ ___       __ _
    \r                            | || __/ __|     / _` |
    \r                            | || |_\__ \    | (_| |
    \r                           |___|\__|___/     \__,_|
    \r                                  _____ _
    \r                                 |_   _(_) ___
    \r                                   | | | |/ _ \ 
    \r                                   | | | |  __/
    \r                                   |_| |_|\___|''')
            # Restart the score count
            user_score = 0
            computer_score = 0
            return_main()


def return_main():
    """
    Return to main menu option through user input.
    """
    # Loop will validate the user input or print invalid option
    while True:
        print("\n")
        choice = input('\nClick "RUN PROGRAM" button to restart or to Main Menu, press (M): ')  # noqa
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
    \n            ______              _____                  ______
    \r        ---'   ____)        ---'  ____)____        ---'   ____)____
    \r              (_____)                ______)                 ______)
    \r              (_____)                _______)             _________)
    \r              (____)                _______)             (____)
    \r        ---.__(___)         ---.__________)        ---.__(___)""")
    # Sets first round and start a loop that counts the rounds
    round = 1
    while round <= 5:
        print(f'''
    \n ---------------------------------------------------------------------
    \r|                             ROUND: {round}                                | # noqa
    \r ---------------------------------------------------------------------
    \r|                    You scored: {user_score} | Computer Scored:{computer_score}                |# noqa
    \r ---------------------------------------------------------------------''')  # noqa
        # Call the function to get user input and checks if user chose gun
        # to break the loop
        user_choice = get_user_input()
        if user_choice != "gun":
            # If gun is not selected then will call computer, results and
            # winner functions until round is reached to 5 so the loop stops
            computer_choice = get_computer_choice()
            result(user_choice, computer_choice)
            winner(round)
        else:
            print("""
    \n           __                                _
    \r          |  |                              | |
    \r          |  |      ___  __ _  ___ _ __   __| |
    \r          |  |     / _ \/ _` |/ _ \ '_ \ / _` |
    \r          |  |____|  __/ (_| |  __/ | | | (_| |
    \r          |_______|\___|\__, |\___|_| |_|\__,_|
    \r                         __/ |
    \r                        |___/""")
            return_main()
            break
        # Round counter
        round = round + 1


def menu():
    """
    Menu functions the will print options for the user
    """
    # Loop will validate input and print options to the user
    while True:
        os.system("clear")
        print("""
        \n               ---------------------- MENU ------------------------
        \r              |                                                     |
        \r              |    Please select one of the following, options:     |
        \r              |                                                     |
        \r              | - Press (S) to Start the Game                       |
        \r              | - Press (R) to see the Rules of the Game            |
        \r              | - Press (C) for credits                             |
        \r              |_____________________________________________________|
        """)
        menu_selection = input("\n              Please select an option: ")
        # Conditionals to check user input and redirect to respective options
        if menu_selection == "S" or menu_selection == "s":
            start_game()
        elif menu_selection == "R" or menu_selection == "r":
            os.system('clear')
            print("""
    \n --------------------------------- HOW TO PLAY --------------------------
    \n  • Game has 5 Rounds
    \r  • Each round you can choose from Rock, Paper or Scissors options
    \r  • Once you have selected one of the options the computer will play
    \r  • Will be printed at the screen if you win or lose that round or a tie
    \r  • A score counter will count the points
    \r  • After the 5th round will be displayed the Winner or Loser of the game
    \r  • Just keep in mind that:
    \r      - Rock beats Scissors
    \r      - Papers beats Rock
    \r      - Scissors beats Paper
    \r  • You might unlock the Fatality mode if you win 3 times put of 5
    \r  • Pay attention to the hints to unluck the MASTER RPS and become Legend
    \r  • Have Fun!""")
            return_main()
        elif menu_selection == "c" or menu_selection == "C":
            os.system("clear")
            print("""
        \n                     This Game was Developed by
        \n                             Cesar Garcia
        \n                       github.com/Cesargarciajr
        \r                 linkedin.com/in/cesar-garcia-637973aa""")
            return_main()
        else:
            print("Invalid input, please try again.")
            time.sleep(1.5)
            continue


def main():
    """
    Main function control the game flow and call the functions
    and start the game
    """
    print("""
    \n                 Welcome to THE ULTIMATE RPS Game!
    \n    Challenge the computer for a 5 round game and see if you can beat it.
    \r               Win 3 times put of 5 to unlock secret!
    \n                      Good Luck and have fun!""")
    print("""
    \n            ______              _____                  ______
    \r        ---'   ____)        ---'  ____)____        ---'   ____)____
    \r              (_____)                ______)                 ______)
    \r              (_____)                _______)             _________)
    \r              (____)                _______)             (____)
    \r        ---.__(___)         ---.__________)        ---.__(___)""")
    # Gives 4.5 second fo the user to read intro message
    print('\nLoading...')
    time.sleep(4.5)
    print('Completed')
    time.sleep(1)
    os.system("clear")
    menu()


# Calling function to Start the Program
main()
