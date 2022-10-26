#Roan Mason
#May 6, 2021
#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 20 and 30 degrees Celsius (inclusive). Unless it is summer, then the upper limit is 35 instead of 30. Ask the user for the current temperature and whether or not it is summer, and output whether or not the squirrels will play.

print("Welcome to Palo Alto!")
temp = int(input("What is the temperature? "))
summer = input("is it summer (Y/N)? ")
summer = summer.upper()#makes input upper ase

if summer == "Y" and temp >= 20 and temp <= 35: #is it summer? if it is then is the temp between 20 and 35 degrees?
    print("The squirrels are playing!")
elif temp >= 20 and temp <= 30: #is the temp between 20 and 30? summer doesnt matter because it was checked in the previous statement
    print("The squirrels are playing!")
else: #if its too hot or too cold then the squirrels arent playing
    print("The squirrels are not playing!")