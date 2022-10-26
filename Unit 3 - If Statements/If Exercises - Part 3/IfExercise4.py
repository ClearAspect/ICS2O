#Roan Mason
#May 6, 2021
#You are driving a little too fast, and a police officer stops you. You recently heard on the news that if you drive 80 km/h or less you won’t get a ticket. But if you drive faster than 80 km/h but less than 100 km/h you will get a small ticket. However, if you drive faster than 100 km/h you will get a big ticket. Unless of course it is your birthday -- on that day, your speed can be 5 km/h higher in all cases. Ask the user for their speed and whether or not it is their birthday, and output whether or not they get no ticket, a small ticket, or a big ticket

print("*****siren noises*****")
speed = int(input("Do you have any idea how fast you were going back there? ")) #ask for user's speed and convert to integer
birthday = input("Id today your birthday (Y/N)").upper() #is it the user's birthday

#set the ticket levels more than upper = big ticket. more than lower and less than upper = small ticket. smaller than upper = no ticket 
lower = 80
upper = 100

if birthday == "Y": #if its the user's birthday leeway is added to the limits
    lower = 85
    upper = 105

if speed <= lower: #less than the lower ticket limit = no ticket
    print("I'll let you off with a warning this time...")
elif speed > lower and speed <= upper: # less than the upper limit and more than the lower limit = small ticket
    print("You were speeding, here's a small ticket for you to pay.")
elif speed > upper: #more than the upper limit = big ticket
    print("Here's a big ticket you speed demon!")