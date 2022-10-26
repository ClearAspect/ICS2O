#Roan Mason
#May 5, 2021
#A computer store sells floppy disks at 50 cents each for small orders or at 30 cents each for orders of 25 disks or more. Write a program that requests the number of diskettes ordered and displays the total cost.

disk_amount = input("How many floppy disks would you like? ")
disk_amount = float(disk_amount)

if disk_amount >= 25: #if the amount of disks being bought is more than 25 then there is a discount added
    unit_cost = 0.30
else:
    unit_cost = 0.50

total_cost = disk_amount * unit_cost#multiplies unit cost by the amount disks being purchase to get the price

print("Unit Cost:","${0:.2f}".format(unit_cost))#ouputs the cost per unit and formats the value
print("Total Cost:","${0:.2f}".format(total_cost))#ouputs the total per unit and formats the value