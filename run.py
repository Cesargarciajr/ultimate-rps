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
            break
        elif user == "p" or user == "P":
            user = "paper"
            break
        elif user == "s" or user == "S":
            user = "scissors"
            break
        elif user == "gun" or user == "Gun" or user == "GUN" or user == "g" or user == "G":
            print(f'''\n You have typed "{user}" and unlocked the Gun. You're the RPS MASTER! YOU WON!!!
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
    Function to compare results and print out the outcome also counts the scores
    """
    global user_score
    global computer_score
    if user == computer:
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
        print(""" \n               You chose: Rock             Computer chose: Scissors
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
        print(""" \n                You chose: Paper           Computer chose: Rock
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
        print(""" \n                You chose: Scissors           Computer chose: Paper
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
        print(""" \n                You chose: Scissors           Computer chose: Rock
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
        print(""" \n                You chose: Paper           Computer chose: Scissors
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
        print(""" \n               You chose: Rock             Computer chose: Paper
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
    global user_score
    global computer_score
    if rounds >= 5: 
        if user_score > computer_score:
            print(f'''\n
            
            
            
            
            
            
            
            
            
                                        CONGATULATIONS YOU WON THE GAME!!!
                                        .-=========-.
                                        \'-=======-'/
                                        _|         |_
            You Scored: {user_score}              ((|   .=.   |))        Computer Scored: {computer_score}
                                        \|   /|\   |/
                                        \__ '`' __/
                                        _`) (´_
                                        _/_______\_
                                        /___________\ ''')
            print('\nTo play again, please click on the "RUN PROGRAM" button')
        elif user_score < computer_score:
            print(f'''\n








    ------------------------------------------------------------------------------
    |                        You scored: {user_score} | Computer Scored: {computer_score}                    |
    ------------------------------------------------------------------------------ 
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
            print('\nTo play again, please click on the "RUN PROGRAM" button')
        else:
            print(f'''





 ------------------------------------------------------------------------------
|                        You scored: {user_score} | Computer Scored: {computer_score}                    |
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
        print('\nTo play again, please click on the "RUN PROGRAM" button')
    
def main():
    """
    Main function control the game flow and call the functions and start the game
    """
    global user_score
    global computer_score
    print("""\n                      Welcome to THE ULTIMATE RPS Game!
             \n     Challenge the computer for a 5 round game and see if you can beat it.
             \r                    Win 3 times in a row to unlock secret!
             \n                           Good Luck and have fun!""")
    print("""
                _______             ______                 _______
            ---'   ____)        ---'  ____)____        ---'   ____)____
                  (_____)                ______)                 ______)
                  (_____)                _______)             _________)
                  (____)                _______)             (____)
            ---.__(___)         ---.__________)        ---.__(___)
        """)
    round = 1
    while round <=5:
        print(f'''
 ------------------------------------------------------------------------------
|                                    ROUND: {round}                                  |
 ------------------------------------------------------------------------------
|                            You: {user_score} | Computer: {computer_score}                              |
 ------------------------------------------------------------------------------''')
        user_choice = get_user_input()
        if user_choice != "gun":
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
            print('\nTo play again, please click on the "RUN PROGRAM" button')
            break
        round = round + 1

main()