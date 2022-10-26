#Roan Mason
#May 19, 2021
#Write a program that displays the sum of all of the odd numbers from 1 to a maximum value entered by the user

num = int(input("Gimmie a number! "))

sum = 0

for i in range (1,num+1,2):
    sum += i

print("The sum of all of the odd numbers from 1 to",num,"is",sum)