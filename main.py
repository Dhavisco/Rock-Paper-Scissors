
import random

while True:
    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ")
    while((user_action != "r") and (user_action != "p") and (user_action != "s")):
        print ("you have entered the wrong input, try again! \n")
        user_action = input("Enter a choice (r for rock, p for paper, s for scissors): ")

    if user_action == "r" :
        user_action = "rock"
    elif user_action == "p" :
        user_action = "paper"
    elif user_action == "s" :
            user_action = "scissors"        
    possible_actions = ["rock", "paper", "scissors"]
    r = "rock"
    p = "paper"
    s = "scissors"
    computer_action = random.choice(possible_actions)
    print(f"\n Player({user_action})  : CPU({computer_action})\n")


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")    
        
    elif user_action == r:
        if computer_action == s:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == p:
        if computer_action == r:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == s:
        if computer_action == p:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

       
    if user_action != computer_action:
        break