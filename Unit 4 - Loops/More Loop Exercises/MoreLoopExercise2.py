#Roan Mason
#May 19, 2021
#Write a program that will display the sum of all of the numbers between two values entered by the user. The program should also display an expression showing what specific numbers were summed.

start = int(input("Enter a starting number: ")) #user input for begining number
end = int(input("Enter a ending number: ")) #user input for ending number
eqn = str(start) #build a string with the starting number
total = start #total of all numbers

while start != end: #as long as the starting number isnt the ending number
    start += 1 #increase the number by one
    eqn += " + "+str(start) #add the new number to the string 
    total += start #add the new number to the total sum

print(eqn,"=",total) #output the final equation and its total properly fotmated