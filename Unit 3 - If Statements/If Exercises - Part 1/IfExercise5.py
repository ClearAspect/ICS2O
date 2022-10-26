#Roan Mason
#May 3, 2021
#Ask the user for 5 numbers.  Count how many are negative.

#ask for numbers and convert them to integers
num1 = input("Enter the first number: ")
num1 = int(num1)
num2 = input("Enter the second number: ")
num2 = int(num2)
num3 = input("Enter the third number: ")
num3 = int(num3)
num4 = input("Enter the fourth number: ")
num4 = int(num4)
num5 = input("Enter the fifth number: ")
num5 = int(num5)

#if a number is below zero then it counts as 1 negative. if not it counts as 0 negatives 
if num1 > 0:
    neg1 = 1
else:
    neg1 = 0
if num2 > 0:
    neg2 = 1
else:
    neg2 = 0
if num3 > 0:
    neg3 = 1
else:
    neg3 = 0
if num4 > 0:
    neg4 = 1
else:
    neg4 = 0    
if num5 > 0:
    neg5 = 1
else:
    neg5 = 0
    
#adds up all counters to display how many negatives there were 
print("You entered",(neg1+neg2+neg3+neg4+neg5),"negative numbers")