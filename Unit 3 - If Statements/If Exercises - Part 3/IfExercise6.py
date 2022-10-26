#Roan Mason
#May 6, 2021
#You keep sleeping in and getting to school late, so you decide to make an alarm clock program. The alarm clock accepts as input the day of the week and whether or not the user is on vacation. On weekdays, the alarm outputs “7:00” as the time to wake up, and “10:00” is outputted on the weekend. However, if the user is on vacation, the alarm outputs “10:00” on weekdays, and “off” on weekends. Try using booleans to simplify your if statements.

'''
weekdays = 7:00 
weekends = 10:00
weekday vaca = 10:00
weekend vaca = off
'''

#asking user for day and if its vacation. convert to uppercase to simplify code
day = input("What day is it? ").upper()
vaca = input("Are you on vacation (Y/N)? ").upper()

if (day == "SATURDAY" or day == "SUNDAY") and vaca == "Y": #is it the weekend and vacation? alarm is off
    print("Alarm turned off!")
elif day == "SATURDAY" or day == "SUNDAY": #is it the weekend only? alarm is set for 10
    print("Alarm set for 10:00")
elif vaca == "Y": #it isnt the weekend but its vacation? alarm is set for 10
    print("Alarm set for 10:00")
else: #it must be a regular weekday. alarm is set for 7
    print("Alarm set for 7:00")