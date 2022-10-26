#Roan Mason
#Apr, 26, 2021
#An employee works 40 hours a week.  They earn $9.58 an hour.  If the employee works more than 40 hours, they receive time and a half.  If the employee works 52 hours, how much would they earn?

reg_hours = 40
total_hours = 52
ot_hours = total_hours - reg_hours
wage = 9.58
ot_pay_multiplier = 1.5
ot_wage = wage * ot_pay_multiplier
reg_week_pay = reg_hours * wage
extra_ot_pay = ot_hours * ot_wage
total_week_pay = reg_week_pay + extra_ot_pay

print("Total Hours","\t","\t",total_hours)
print("Regular Hours","\t","\t",reg_hours)
print("OT Hours","\t","\t",ot_hours)
print("Regular Rate","\t","\t","${0:.2f}".format(wage))
print("OT Rate","\t","\t","${0:.2f}".format(ot_wage))
print("Total Regular Pay","\t","${0:.2f}".format(reg_week_pay))
print("Total OT Pay","\t","\t","${0:.2f}".format(extra_ot_pay))
print("Total Pay","\t","\t","${0:.2f}".format(total_week_pay))