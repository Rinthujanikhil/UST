#3. Create a program to play RPS Game

#Inputs:
#1. Enter Player name 1
#2. Enter Player name 2
#3. Enter Player 1 Choice
#4. Enter Player 2 Choice


#Choices are "Rock", "Scissor", "Paper"

#result: who wins?


#display result: Player name with choice Rock wins
#Player name with choice Scissor Lose


#how to manipulate result:
#If P1 enter Rock and P2 enters Scissor then P1 Wins
#if P1 enter Rock and P2 enters Paper then P2 Wins
#if P1 enter Scissor and P2 enters Paper then P1 wins
#if both player enters the same choice it should say "Tie"


player1=str(input("Enter player1 name:"))
player2=str(input("Enter player2 name:") )           
player1_choice=str(input("enter the choice:"))
player2_choice=str(input("enter the choice2:"))
if player1_choice == player2_choice:
    print(f"Both players selected {user_action}. It's a tie!")
elif player1_choice == "rock":
    if player2_choice == "scissors":
        print("Rock smashes scissors! player1 win!")
    else:
        print("Paper covers rock! player2 win.")
elif player1_choice == "paper":
    if player2_choice == "rock":
        print("Paper covers rock! player1 win!")
    else:
        print("Scissors cuts paper! player2 win.")
elif player1_choice == "scissors":
    if player2_choice == "paper":
        print("Scissors cuts paper! player1 win!")
    else:
        print("Rock smashes scissors! player2 win.")

        
