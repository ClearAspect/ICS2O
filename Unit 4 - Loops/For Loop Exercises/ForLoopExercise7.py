#Roan Mason
#May 9, 2021
#Write a Python program that will use a for loop to ask the user for 5 numbers and count how many are negative

count = 0

for i in range(5,0,-1):
    num = int(input("Enter a number (" + str(i) + " to go): "))
    if num < 0:
        count = count + 1

print("You entered "+ str(count)+" negative numbers")