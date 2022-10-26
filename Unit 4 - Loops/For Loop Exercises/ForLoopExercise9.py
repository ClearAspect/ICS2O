#Roan Mason
#May 9, 2021
#Generate 1000 random numbers between 1 and 5. Display a chart showing the number of times each number was generated
import random

#create counters for numbers 1-5 starting at zero. for later 
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(1000): #generate 100 things
    n = random.randrange(5) + 1#generate 1000 numbers 1-5
    if n == 1: #check if a number 1-5 is randomized. for each elif statement bellow
        num1 += 1
    elif n == 2:
        num2 += 1
    elif n == 3:
        num3 += 1
    elif n == 4:
        num4 += 1
    elif n == 5:
        num5 += 1        

print("Number\t# of Times")
print("1\t\t",(num1))#prints the number of times a number was counted in the randomization
print("2\t\t",(num2))
print("3\t\t",(num3))
print("4\t\t",(num4))
print("5\t\t",(num5))