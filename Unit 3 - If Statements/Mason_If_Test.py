#Roan Mason
#May 7, 2021
#Generate a random number between 1 - 100. Ask the user to enter two guesses. Tell them if they guess correctly, or which guess was the closest.
'''
equally close to number
make statement for cloest number
make statement for correct guess
'''

import random
import math

r_num = random.randint(1,101)
print(r_num)
num1 = int(input("Enter your first guess: "))
num2 = int(input("Enter your second guess: "))
a_num1 = math.fabs(r_num - num1)
a_num2 = math.fabs(r_num - num2)



if a_num1 == a_num2:
    print("Nope! your guesses of",num1,"and",num2,"were equally close to",r_num)
elif (num1 or num2) == r_num:
    print("You correctly guessed",r_num,"!")
elif a_num1 < a_num2:
    print("Nope! your guess of",num1,"was closer to",r_num)
elif a_num1 > a_num2:
    print("Nope! your guess of",num2,"was closer to",r_num)
