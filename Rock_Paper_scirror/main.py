""" 
WORKFLOW OF PROJECT:
1- Input from user (Rock , Ppaper , Scissors)
2- Computer will randomly select one of the three options
3- Compare the user input and computer selection to determine the winner
4- Display the result to the user (win, lose, or draw)

cases:
A - Rock 
Rock vs Rock = Draw
Rock vs Paper = Paper wins 
Rock vs Scissors = Rock wins 


B - Paper
Paper vs Rock = Paper wins
Paper vs Paper = Draw
Paper vs Scissors = Scissors wins

C - Scissors
Scissors vs Rock = Rock wins
Scissors vs Paper = Scissors wins
Scissors vs Scissors = Draw


"""
import random 
item_list = ["rock", "paper", "scissors"]
user_choice = input ("enter youe choice (rock, paper, scissors): ")
computer_choice = random.choice(item_list)

print(f"user choice: {user_choice} , computer choice : {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")



