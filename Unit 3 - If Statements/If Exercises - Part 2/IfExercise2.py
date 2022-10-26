#Roan Mason
#May 5, 2021
#Write a program that asks the user for a number and tells them whether it’s even or odd

number = input("Enter a number! ")
number = int(number)

remainder = number % 2

if remainder == 1:#if there is a remainder the number is an odd number. if there isnt it is even
    print(number,"is odd!")
else:
    print(number,"is even!")