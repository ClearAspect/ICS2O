#Roan Mason
#April 27, 2021
#Ask the user to enter two numbers. Output the results of addition, subtraction, multiplication, division, modulus, and exponent. Display the results accurate to one decimal place.

'''
IPO Chart
INPUT
input numbers used for calculations
PROCESSING
use numbers and calculated all types of simple equations
OUTPUT
display all types of calculations
'''

import math
#get inputs and convert them to float values
s_num1 = input("Please enter the first number: ")
s_num2 = input("Please enter the second number: ")
num1 = float(s_num1)
num2 = float(s_num2)

#use inputs for calculations
add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
remain = num1 % num2
power = num1 ** num2

print("{0:,.1f}".format(num1),"+","{0:,.1f}".format(num2),"=","{0:,.1f}".format(add))
print("{0:,.1f}".format(num1),"-","{0:,.1f}".format(num2),"=","{0:,.1f}".format(sub))
print("{0:,.1f}".format(num1),"x","{0:,.1f}".format(num2),"=","{0:,.1f}".format(multi))
print("{0:,.1f}".format(num1),"/","{0:,.1f}".format(num2),"=","{0:,.1f}".format(div))
print("{0:,.1f}".format(num1),"%","{0:,.1f}".format(num2),"=","{0:,.1f}".format(remain))
print("{0:,.1f}".format(num1),"^","{0:,.1f}".format(num2),"=","{0:,.1f}".format(power))