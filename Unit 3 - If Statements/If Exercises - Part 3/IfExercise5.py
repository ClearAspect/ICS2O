#Roan Mason
#May 6, 2021
#Ask the user for two numbers and output their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just output 20

#ask for numbers and convert them to integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total = num1 + num2 #add the inputed numbers to get the sum

if total >= 10 and total <= 19: #if the sum is in the range of 10-19 inclusive than the sum will = 20
    print("The sum of", num1 ,"and", num2 ,"is 20")
else: #if sum does not range in 10-19 inclusive than nothing happens to the sum
    print("The sum of", num1 ,"and", num2 ,"is",total)