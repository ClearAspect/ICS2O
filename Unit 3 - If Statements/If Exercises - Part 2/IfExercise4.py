#Roan Mason
#May 5, 2021
#Write a program that asks the user for three numbers and tells them which one is the smallest.

num1 = input("Enter the first number please: ")
num1 = float(num1)

num2 = input("Enter the second number please: ")
num2 = float(num2)

num3 = input("Enter the third number please: ")
num3 = float(num3)


if num1 <= num2 and num1 <= num3:#Checks if num1 is smaller or equal to any of the other numbers.
    print(num1,"is the smallest number")#if num1 is the smallest it only prints this saying so.
#these comments are also relevent for the rest of the if statements
elif num2 <= num1 and num2 <= num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")