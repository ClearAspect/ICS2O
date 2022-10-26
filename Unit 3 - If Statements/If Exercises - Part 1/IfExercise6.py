#Roan Mason
#May 3, 2021
#Write a program that will determine the net profit or loss of a company. If there are more Expenses than there is Revenue then the end result is a negative number.  Your program should ask the user for the revenue and expenses.  Print a statement based on the result, which says either “You earned a profit of...”, or “You suffered a loss of ...”

rev = input("How much was your revenue? ")
rev = float(rev)
exp = input("How much were your expenses? ")
exp = float(exp)

if rev > exp:
    print("You earned a profit of","${0:.2f}".format(rev - exp))
else:
    print("You suffered a loss of","${0:.2f}".format(exp - rev))