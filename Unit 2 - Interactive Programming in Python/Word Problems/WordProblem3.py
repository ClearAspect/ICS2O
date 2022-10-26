#Roan Mason
#Apr, 26, 2021
#A factory produces 1,022,957 widgets per day. They sell them in packages of 12.  How many packages are produced in a day?  Indicate how many full boxes are required and how many widgets would be left in a partially filled box

widgets_per_day = 1022957
widgets_per_package = 12
amount_in_leftover = widgets_per_day % widgets_per_package
total_full_boxes = (widgets_per_day - amount_in_leftover) / widgets_per_package #remove remander to get whole number


print("Total Widgets","\t","\t", widgets_per_day)
print("Number in Pack","\t","\t", widgets_per_package)
print("Total Full Boxes","\t", "{0:.1f}".format(total_full_boxes))#adding decimal place 
print("Amount in partial box","\t", amount_in_leftover)

