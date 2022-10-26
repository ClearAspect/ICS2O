#Roan Mason
#May 18, 2021
#Repeatedly ask the user for a number.  Count how many times it takes until the user enters a negative number. Stop asking for numbers when a negative is entered.

num = 0 #create variable for input later. otherwise code wont work. set it to anything but a negative to that the loop starts
count = 0 #create a counter for the amount of inputs

while num >= 0: #as long as the number isnt negative the loop will continue
    num = int(input("Enter a number: ")) #ask the user for a number
    count += 1 #add to the count everytime a guess is made
    if num < 0: #if the number entered is a negative the print how many times it took to guess a negative
        print("You took",count,"tries to enter a negative")