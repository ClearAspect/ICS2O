#Roan Mason
#April 27, 2021
#Ask the user for the name of an item, it’s price and quantity ordered. Calculate and display the total price before tax, and after tax. (HST = 13%). Then ask the user for the amount they will be paying with. Display the amount of change they are to receive.
# tax is = 13%

'''
IPO Chart
INPUT
take in item name, price and amount of items
PROCESSING
based on input values calculate total before tax, amount of tax, total after tax and change due
OUTPUT
display total before tax, amount of tax, total after tax and change due
'''

#inputs
item_name = input("What is the name of the item you are buying? ")
s_item_cost = input("How much does a "+item_name+" cost? ")
s_amount_of_items = input("How many "+item_name+"s are you buying? ")
#convert numbers to floats
item_cost = float(s_item_cost)
amount_of_items = float(s_amount_of_items)

#creating ouput values with math
total = item_cost * amount_of_items
tax = total * 0.13
tax_total = total + tax
#displaying cost information and formating it
print("Total before tax:\t","${0:,.2f}".format(total))
print("Amount of tax:\t\t","${0:,.2f}".format(tax))
print("Total after tax:\t","${0:,.2f}".format(tax_total))

#Inputing payment and calculating change
s_payment = input("Please enter the amount you will be paying: ")
payment = float(s_payment)

#calculates change due and formats money
#if else to see if enough funds are entered into input
if payment > tax_total:
    change_due = payment - tax_total
    print("Change due:\t\t","${0:,.2f}".format(change_due))
    print("Thank you for your business!")
else:
    print("Insuffecient Funds")