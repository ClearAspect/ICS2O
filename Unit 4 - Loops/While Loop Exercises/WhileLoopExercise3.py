#Roan Mason
#May 18, 2021
#Ask the user for several names.  Count how many names were entered.  The name “Done” can be used to indicate the user wishes to stop entering.  Do not count “Done” as one of the names. Display a list of all the names after the user is finished.

count = 0 #create counter for the number of names
names = ("Here they are:\n") #create a varible to store names and display theme later
name = "none" #make anything but "Done" so the loop will begin

while name != "Done": #if the name entered isnt "Done" than ask for another name
    name = input("Gimmie a name: ")
    if name == "Done": #if the name entered is "Done" then tell the user the number of different names entered and what they were by using the "names" variable containing them
        print("You entered",count,"names")
        print(names)    
    if name in names: #if a name entered is in list already than do nothing at all
        pass
    else: #if none of the previous conditions are true than its safe to add a new name to the list and increase the counter
        names += name + "\n"
        count += 1

