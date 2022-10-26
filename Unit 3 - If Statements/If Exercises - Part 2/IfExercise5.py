#Roan Mason
#May 5, 2021
#Write a program that asks the user for three numbers. Determine how many of them are equal to each other.

num1 = input("Enter the first number please: ")
num1 = float(num1)

num2 = input("Enter the second number please: ")
num2 = float(num2)

num3 = input("Enter the third number please: ")
num3 = float(num3)

if num1 == num2 == num3: #If all three numbers are the same than this is outputed
    print("All three are the same!")
elif num1 == num2 or num2 == num3 or num3 == num1: #If none are the same than it checks if any combo of numbers are equal than this is outputed
    print("Two were the same!")
else: #If none of the previous checks are true than this is outputed
    print("All were different!")