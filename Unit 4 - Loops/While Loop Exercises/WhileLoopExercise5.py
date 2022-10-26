#Roan Mason
#May 18, 2021
#Make a number guessing game. Generate a random number from 1 - 100 and ask the user to guess it. To help them guess more accurately, tell the user if their guess was too high or too low after each incorrect guess

import random

randnum = random.randint(1,100)
guess = 0

print("I'm thinking of a number between 1 and 100...")
while guess != randnum:
    guess = int(input("Enter a guess: "))
    if guess > randnum:
        print("Too high!")
    elif guess < randnum:
        print("Too low!")
    else:
        print("You got it!")