#Roan Mason
#May 3, 2021
#Write a program that will calculate a salesperson's salary including commission.  Ask the user for their name and weekly sales.  If they made over $200 in sales they earn an extra 5% of sales.  Everyone earns $300 per week as their base pay. Calculate the person's final pay.

#ask for name and sales. then convert sales to integer
name = input("Enter your name: ")
sales = input("Enter your sales: ")
sales = int(sales)

#if sales are more than 200 than create extra. if its not than make the extra zero
if sales > 200:
    extra = sales * 0.05
else:
    extra = 0

#print the salary and format the money. 300 is regular pay. extra is the 5% if you had 200+ in sales
print(name,"'s salary is","${0:.2f}".format(300 + extra))