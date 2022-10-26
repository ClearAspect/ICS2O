#Roan Mason
#May 19, 2021
#Write a program that calculates the average of the product of all of the numbers from 1 to a number entered by a user.

num = int(input("Gimmie a number! "))

product = 1

for i in range (2,num+1):
    product *= i

avg = product / num

print("The product of all of the numbers from 1 to",num,"is",product)
print("and average of this product is",avg)