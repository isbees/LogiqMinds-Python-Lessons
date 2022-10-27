'''
We will learn about:
    - While loops and how to use them
    - compare while loops to for loops
    - Boolean values
        - True / False
        - Comparisons like ==, <, <=, >, >=
'''

import random

def knock_knock():
    # first input
    a = input('Knock, knock!\n')

    # second input
    if (a == "Who's there" or a == "who's there" or a == "Who's there?" or a == "who's there?"):
        b = input('Orange\n')
    else:
        print("Please print 'Who's there?'\n")
        return
    
    #response
    if (b == "Orange who?" or b == "orange who?" or b == "Orange who" or b == "orange who"):
        c='Orange you going to let me in?'
        print(c)
    else:
        b=raw_input("Please print 'Orange who?'\n")
        if (b=="Orange who?" or b=="orange who?" or b=="Orange who" or b=="orange who"):
            c='Orange you going to let me in?'
            print(c)

def rock_paper_scissors():
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    print()

def math_game():
    x = random.randint(0,100)
    y = random.randint(0,100)
    
    ans = input(f"What is {x} + {y}?\n")

    if (x+y) == int(ans):
        print("Correct!\n")
    else:
        print("Incorrect!\n")

running = True

# this is a game menu
while running:
    choice = input("Choose a game:\n1) Knock Knock (type\'k\')\n2) Rock-Paper-Scissors (type\'rps\')\n3) Math Solver (type\'m\')\n")
    
    if choice == 'k':
        print("You chose: Knock Knock")
        knock_knock()

    elif choice == 'rps':
        print("You chose: Rock Paper Scissors")
        rock_paper_scissors()

    elif choice == 'm':
        print("You chose: Math Solver")
        math_game()
    
    else:
        print("Not an option! please enther a correct option")
    # ideas for games: math solver, Knock Knock, 
    