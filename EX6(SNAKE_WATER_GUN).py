"""
Docstring for EX6(SNAKE_WATER_GUN)
snake - water = snake
gun - water = water
gun - snake = gun

10 times
computer, user win count
while loop
"""
import random

game = ["S","W","G"]
game_count = 1
computer_win = 0
user_win = 0

print("Welcome to Snake Water Gun game \n Here are the rules : \n 1.) snake - water = snake \n 2.)gun - water = water " \
    "\n 3.) gun - snake = gun")

while(game_count<=10):
    print("Enter your choice \n S for Snake, W for water, G for gun")
    user_choice = input().capitalize()
    computer_choice = random.choice(game)
    print(f"Computer choice is {computer_choice}")
   
    # game_count+=1
    if user_choice==computer_choice:
        print("Draw")

    elif(user_choice=="S" and computer_choice=="W" or 
        user_choice=="G" and computer_choice=="S" or
        user_choice=="W" and computer_choice=="G"):
        user_win+=1
        print("Win")

    else:
        computer_win+=1
        
        print("Lose")
    game_count+=1

    print(f"You won {user_win} times and computer won {computer_win} times")

if(computer_win>user_win):
    print("YOU LOSEEE")
elif(user_win>computer_win):
    print("YOU WINNNN BUBUUEEEE")
else:
    print("DRAWWW")

 # if(user_choice == "S"):
    #     if(computer_choice == "W"):
    #         user_win+=1
    #         print("Win")
    #     elif(computer_choice == "G"):
    #         computer_win+=1
    #         print("Lose")
    #     else:
    #         print("Draw")
    #     print(f"Your score = {user_win}  \n Computer score = {computer_win}")

    # elif(user_choice == "G"):
    #     if(computer_choice == "S"):
    #         user_win+=1
    #         print("Win")
    #     elif(computer_choice == "W"):
    #         computer_win+=1
    #         print("Lose")
    #     else:
    #         print("Draw")
    #     print(f"Your score = {user_win}  \n Computer score = {computer_win}")
        
    # elif(user_choice == "W"):
    #     if(computer_choice == "G"):
    #         user_win+=1
    #         print("Win")
    #     elif(computer_choice == "S"):
    #         computer_win+=1
    #         print("Lose")
    #     else:
    #         print("Draw")
    #     print(f"Your score = {user_win}  \n Computer score = {computer_win}")
  