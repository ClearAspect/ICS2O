#Roan Mason
#May 6, 2021
#The number 4 is a truly great number. Ask the user for two numbers and output “Great”  if either one is 4. Also output “Great”  if their sum or difference is 4. Otherwise output “Not so great”. Note: math.fabs(number), returns the absolute value of a number
import math

#ask for numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


add = num1 + num2 #add 2 numbers
sub = num1 - num2 #subtract the 2
sub = int(math.fabs(sub)) #create the difference into absolute value 

if sub == 4 or sum == 4: #if the sum or difference's absolute value = 4 than print great 
    print("Great!")
elif num1 == 4 or num2 == 4: #if either number is 4 than print great 
    print("Great!")
else: #any other conditions = not so great
    print("Not so Great")