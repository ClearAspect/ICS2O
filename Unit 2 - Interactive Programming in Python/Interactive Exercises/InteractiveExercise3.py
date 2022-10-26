#Roan Mason
#April 27, 2021
#Ask the user for a Fahrenheit temperature. Display the equivalent temperature in Celsius
#(F - 32) x .5556

#ask for Temp in F
s_fahr = input("Please enter a temperature in Fahrenheit: ")
#convert to float value
fahr = float(s_fahr)

#convert to Celcius
cel = ((fahr - 32) * (5 / 9))
#display answer and format decimal
print(fahr,"degrees Fahrenheit equals","{0:.1f}".format(cel),"degrees Celcius")