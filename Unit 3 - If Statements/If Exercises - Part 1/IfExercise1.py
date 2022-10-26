#Roan Mason
#May 3, 2021
#Write a program to find the larger of two numbers inputted by the user

#asks for numbers and converts them to integers
s_num1 = input("Enter the first number: ")
num1 = int(s_num1)

s_num2 = input("Enter the second number: ")
num2 = int(s_num2)

#checks if numbers are equal. if they arent than it checks if the first number is bigger.
if num1 == num2:
    print(num1,"is the same as",num2)
elif num1 > num2:
    print(num1,"is bigger than",num2)
else:#if the first number is smaller than this line is printed saying so.
    print(num2,"is bigger than",num1)
