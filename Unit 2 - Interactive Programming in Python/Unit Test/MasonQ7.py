#Roan Mason
#May 4, 2021
#Write an interactive program that will determine the percentage increase/decrease of any product given its name and the two different prices.

itemname = input("Enter the name of the item: ") 
old_cost = input("Enter what the "+itemname+" used to cost: ")
old_cost = int(old_cost)
new_cost = input("Enter what the "+itemname+" costs now: ")
new_cost = int(new_cost)

per_change = ((new_cost / old_cost) * 100) - 100
print("The price changed by","{0:.1f}%".format(per_change))
