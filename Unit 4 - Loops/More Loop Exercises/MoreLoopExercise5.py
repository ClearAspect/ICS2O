#Roan Mason
#May 19, 2021
#Write a program that will help the user to analyze their bowling scores. The user can enter as many scores as they like, and will enter -1 when they are done entering scores. Your program will then display the highest, lowest, and average score entered.

count = 0 #count for the amount of times a number is entered
average = 0 #start a variable for average
score = 0 #start a variable for the score
lowest = 301 #highest possible score
highest = 0 #lowest possible score

while score != -1: #as long as the score isnt -1.(-1 stops the loop and ends the program)
    score = int(input("Enter a bowling score: ")) #user inputs the scores
    if score != -1: #fail safe to stop -1 from entering in as a number in the count and average
        count += 1
        average += score
        if score > highest: #the highest possible score must be more than the lowest possible score. everytime the loop restarts it checks if the new number is bigger than the last highest score
            highest = score
        if score < lowest:#the lowest possible score must be less than the highest possible score. everytime the loop restarts it checks if the new number is smaller than the last lowest score
            lowest = score

average = average / count #simple calculation for average(total score divided by # of scores entered)

#output values to user once everything is done
print("You entered",count,"bowling scores.")
print("The best score entered was",highest)
print("The worst score entered was",lowest)
print("The average score entered was","{0:,.1f}".format(average)) #format average so that its not a repeating decimal