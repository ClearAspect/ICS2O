#Roan Mason
#May 18, 2021
#Ask the user for the capital of Indonesia. Count how many incorrect guesses it takes until the correct answer is entered.

answer = "" #create variable for input later. otherwise code wont work.
count = -1 #create a counter for the amount of inputs. -1 so the final correct guess isnt counted

while answer != "Jakarta": #as long as the input isnt the answer the question will be asked again and the counter will increase for each guess after conditions are checked
    answer = input("What's the capital of Indonesia? ")
    count += 1
    if answer == "Jakarta": #if the guess is correct than the user will be told they are correct and the amount of times they got it wrong
        print("Correct!")
        print("You guessed wrong",count,"times")
    else: #anything else besides "Jakarta" must be wrong
        print("Incorrect!")