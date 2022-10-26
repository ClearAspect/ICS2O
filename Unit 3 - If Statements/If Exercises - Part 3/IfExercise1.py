#Roan Mason
#May 6, 2021
#When monkeys get together for a party, they like to have bananas. A monkey party is successful when the number of bananas is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of bananas. Ask the user for a number of bananas, and if it’s the weekend. Output whether or not the party was successful.

print("\"@('o')@\"Welcome to the monkey party")
bananas = int(input("How many bananas did you bring? "))
day = input("is it the weekend (Y/N)? ")
day = day.upper()#makes input upper ase

if day == "Y" and bananas >= 40:#is it the weekend and is there more than 40 bananas
    print("The party is a success!")
elif bananas >= 40 and bananas <= 60: #is the number or bananas between 40 and 60. weekend doesnt matter because it was check in the previous statement
    print("The party is a success!")
else: #must not have been successful
    print("The party is unsuccessful...")