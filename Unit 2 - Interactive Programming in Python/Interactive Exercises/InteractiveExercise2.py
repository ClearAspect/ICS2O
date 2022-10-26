#Roan Mason
#April 27, 2021
#Ask the user for a Celsius temperature. Display the equivalent temperature in Fahrenheit
#(Cel × 1.8) + 32

#ask for Temp in C
s_cel = input("Please enter a temperature in Celcius: ")
#convert to float value
cel = float(s_cel)

#convert to Fahrenheit
fahr = (cel * (9 / 5)) + 32
#display answer and format decimal
print(cel,"degrees Celcius equals","{0:.1f}".format(fahr),"degrees Fahrenheit")