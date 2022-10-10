#snake, gun and water game

player1=str(input("Enter player1 name:"))
player2=str(input("Enter player2 name:") )           
player1_choice=str(input("enter the choice:"))
player2_choice=str(input("enter the choice2:"))
if player1_choice!='snake' and player1_choice !='water' and player1_choice!='gun' and player2_choice!='snake' and player2_choice !='water' and player2_choice!='gun':
    print("unvalide choice")
if player1_choice == player2_choice:
    print("Both players selected . It's a tie!")
    
    
if player1_choice == "snake":
    if player2_choice == "water":
        print("snake drink water! player1 win!")
    elif player2_choice=="gun":
        print("Gun shoot the snake player2 win")

if player1_choice == "water":
    if player2_choice == "gun":
        print("gun cannot shoot throw water player1 win!")
    elif player2_choice=="snake":
        print(" snake drink water player2 win")
        
if player1_choice == "gun":
    if player2_choice == "snake":
        print("Gun shoot the snake player1 win!")
    elif player2_choice=="water":
        print(" gun cannot shoot throw water player2 win")
