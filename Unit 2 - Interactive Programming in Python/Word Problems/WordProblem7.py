#Roan Mason
#Apr, 26, 2021
#An item in a store is priced at $62.99.  The cost of the item including sales tax is $71.81.  What is the dollar amount of sales tax and what percent of sales tax was imposed on the item?

item_cost = 62.99
item_plus_tax = 71.81
amount_of_tax = item_plus_tax - item_cost
tax_rate = (amount_of_tax / item_cost) * 100 #multiply by 100 to get the percentage as a whole number

print("Original Cost","\t","${0:.2f}".format(item_cost))
print("Final Cost","\t","${0:.2f}".format(item_plus_tax))
print("Amount of Tax","\t","${0:.2f}".format(amount_of_tax))
print("Rate of Tax","\t","{0:.0f}%".format(tax_rate))