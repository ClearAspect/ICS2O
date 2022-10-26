#Roan Mason
#May 19, 2021
#Write a program that allows the user to determine for how long they will need to invest their money in order to reach a desired target amount. The user will provide the initial amount of money they are to invest, as well as their annual interest rate. They will also provide their desired target amount. Using this information, output a chart which shows the user how many years their investment will take to reach the target value.

depo = int(input("How much $ are you initially depositing? "))  #how much is the user depositing
inter_rate = int(input("And what's your interest rate (as a %, i.e. 10 = 10%)? ")) #whats the interest rate
inter_rate = inter_rate / 100 #convert the rate into a percentage
goal = int(input("How much $ are you wanting to end up with? ")) #whats the $ goal of the user

inter_earned = depo * inter_rate #interest earned is the rate times the amount invested
year = 0 #create a counter for the year

print("Year\tStarting Value\tInterest Earned\tEnding Value") #simple print statement to start a chart
while depo <= goal: #as long as the investment doesnt reach the goal the following occours
    inter_earned = depo * inter_rate #interest earned is the rate times the amount invested. This increases every year because of compound interest(intrest on intrest)
    depo += inter_earned #investments final value is the interest earned and the amount deposited
    starting = depo - inter_earned #this is each years starting value
    year += 1 #each time the loop occours a year has passed and the counter increases
    print(str(year)+"\t"+"${0:,.2f}".format(starting)+"\t"+"${0:,.2f}".format(inter_earned)+"\t"+"\t"+"${0:,.2f}".format(depo)) #outputs the year, Starting year value, interest earned, and Ending value all formated and lined in a chart.

print("in "+ str(year) +" years, you'll have meet your goal!") #simple print command that says the amount of years that passed until the investment reached the goal