#Roan Mason
#April 27, 2021
#Ask the user for the lengths of four long jumps. Display the sum and average of these four jumps

'''
IPO Chart
INPUT
The distance of the 4 jumps
PROCESSING
Calculate Total length of jumps and average distance
OUTPUT
Display Total length of jumps and average distance
'''

#inputing jump distances
s_j1 = input("Enter the length of your first jump: ")
s_j2 = input("Enter the length of your second jump: ")
s_j3 = input("Enter the length of your third jump: ")
s_j4 = input("Enter the length of your fourth jump: ")
#convert to float value
j1 = float(s_j1)
j2 = float(s_j2)
j3 = float(s_j3)
j4 = float(s_j4)

#calculate outputs
jump_total = (j1 + j2 + j3 + j4)
jump_average = (j1 + j2 + j3 + j4) / 4

print("The total of your four jumps is:",jump_total)
print("The average of your four jumps is:",jump_average)