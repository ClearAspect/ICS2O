#Roan Mason
#April 27, 2021
#Ask the user for the length and width of a rectangle. Display the area and perimeter of the rectangle

#get values as strings via input
s_length = input("Please enter the length of your rectangle: ")
s_width = input("Please enter the width of your rectange: ")

#convert strings to float value to do math
length = float(s_length)
width = float(s_width)

#calculate rectangle area and perimeter then print it
area = length * width
perimeter = (length + width) * 2

print("The rectangle has an area of", area ,"and a perimeter of", perimeter)