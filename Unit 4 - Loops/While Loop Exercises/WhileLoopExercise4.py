#Roan Mason
#May 18, 2021
#Ask the user for a dollar amount of deposit and rate of interest.  Determine how many years it would take to become a millionaire.  Output a chart similar to the one below.

depo = int(input("How much $ are you depositing? ")) #how much is the user depositing
inter_rate = int(input("And what's your interest rate (as a %, i.e. 10 = 10%)? ")) #whats the interest rate
inter_rate = inter_rate / 100 #convert the rate into a percentage

inter_earned = depo * inter_rate #interest earned is the rate times the amount invested
year = 0 #create a counter for the year

print("Year\tInterest Earned\tInvestment Value") #simple print statement to start a chart
while depo <= 1000000: #as long as the investment doesnt reach 1 million dollars the following occours
    inter_earned = depo * inter_rate #interest earned is the rate times the amount invested. This increases every year because of compound interest(intrest on intrest)
    depo += inter_earned #investments final value is the interest earned and the amount deposited 
    year += 1 #each time the loop occours a year has passed and the counter increases
    print(str(year)+"\t"+"${0:,.2f}".format(inter_earned)+"\t"+"${0:,.2f}".format(depo)) #outputs the year, interest earned, and investment value all formated and lined in a chart.

print("in only "+ str(year) +" Years you'll be a millionaire!") #simple print command that says the amount of years that passed until the investment reached a million dollars