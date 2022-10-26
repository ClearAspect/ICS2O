#Roan Mason
#May 19, 2021
#Create a slot machine program. The user starts with 100 tokens. With each pull of the handle, the user loses 1 token and the computer spins 3 wheels, each consisting of the number 1, 2 and 3. If all three numbers are 1, the user gets 4 tokens; if all are 2, the user gets 8 tokens; if all are 3, the user gets 12 tokens. Display the number of tokens to the user after each pull, and the result of each spin should also be displayed. The program ends when the user is either out of tokens, or decides to walk away.

import random

tokens = 100 #Starting tokens

play = "spin" #make spin so game starts

while play == "spin": #if its spin game starts
    print("You have",tokens,"tokens") #prints your token count
    play = input("Would you like to spin or leave? ") #asks if you want to continue to play
    if play == "spin" and tokens > 0: #if you want to play, the game starts
        num1 = random.randint(1,3) #create 3 random numbers 1, 2, or 3
        num2 = random.randint(1,3)
        num3 = random.randint(1,3)
        print("Spin Results\n",num1,"-",num2,"-",num3) #show your spin of numbers
        tokens -= 1 #take away a token for spining
        if num1 == 1 and num2 == 1 and num3 == 1: #if there are 3 1's you win 4 tokens
            tokens += 4
        elif num1 == 2 and num2 == 2 and num3 == 2: #if there are 3 2's you win 8 tokens
            tokens += 8
        elif num1 == 3 and num2 == 3 and num3 == 3: #if there are 3 3's you win 12 tokens
            tokens += 12
            #anything else is a loss
    else: 
        print("You ran out of tokens or typed the wrong word...")
if play != "spin": #if you type "leave" or anything else it displays your final winning/loss and thanks you
    print("Thanks for playing!")
    print("You finished with",tokens,"tokens")