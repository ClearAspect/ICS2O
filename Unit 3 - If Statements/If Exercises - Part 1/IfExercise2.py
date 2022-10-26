#Roan Mason
#May 3, 2021
#Write a program that will ask the user for a number.  If the number entered is negative, display a message (i.e. “X is a negative number”).

#asks for number and converts it to a integer
num = input("Enter a number please: ")
num = int(num)

#checks if the entered number is smaller then zero to determine whether its negative or not. if not another print line is outputed saying so.
if num < 0:
    print(num,"is a negative number.")
else:
    print(num,"is not a negative number")