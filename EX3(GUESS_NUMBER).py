n = 18
no_of_guess = 5
print("Welcome to the guessing game \nYou have ",no_of_guess," to guess" 
"the number. The number will be between 1 to 30")


i = 0
while(i<no_of_guess):
    print("Enter your guess")
    guess = int(input())
    i=i+1
    print("You have ",(no_of_guess-i),"guess left")

    if(n==guess):
        print("Congratulations you have won!!")
        print("You guessed it in ",i,"chances")
        break
    
    elif(n>guess):
        print("Your guess is lower")
        continue
        
    else:
        print("Your guess is greater")
        continue
if(i>4):
    print("GAME OVER")