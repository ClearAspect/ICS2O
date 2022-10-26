#Roan Mason
#May 5, 2021
#3. Write a program that will ask the user for their name, total hours worked and regular rate of pay. Overtime pay is double the regular rate of pay. If a person works more than 40 hours, they get overtime (otherwise they don’t).  Calculate the user's gross pay. (Note-the user might work 2 hours a week, the user might work 42 hours a week).

name = input("What is your name? ")
hours = input("How many hours did you work this week " + name + "? ")
hours = float(hours)
reg_rate = input("And what is your regular rate of pay? ")
reg_rate = float(reg_rate)

if hours > 40: #check if person worked OT
    ot_hours = hours - 40 #removes regular hours to get the OT hours
    reg_hours = 40 #non OT hours
else: #no OT hours worked
    reg_hours = hours #hours inputed is used
    ot_hours = 0 #less than 41 hours worked so no OT
ot_rate = reg_rate * 2 #the rate of OT is equal to the normal rate * 2. (Real Ontario rate is "time and a half" not double)
ot_pay = ot_hours * ot_rate #OT hours times OT rate is your extra pay for working OT

reg_pay = reg_hours * reg_rate #your rate times hours worked = weekly pay
gross_pay = reg_pay + ot_pay #total pay due to you

print("\nFINANCIAL REPORT FOR",name.upper())
print("_________________________")
print("Regular Hours:",reg_hours)
print("Regular Rate:","${0:,.2f}".format(reg_rate))
print("Regular Pay:","${0:,.2f}".format(reg_pay))
print("_________________________")
print("OT Hours:","{0:.0f}".format(ot_hours))
print("OT Rate:","${0:,.2f}".format(ot_rate))
print("OT Pay:","${0:,.2f}".format(ot_pay))
print("_________________________")
print("Gross Pay:","${0:,.2f}".format(gross_pay))