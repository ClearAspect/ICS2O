#Roan Mason
#May 5, 2021
#Create your own quiz with five or more questions. Keep track of the users score, and at the end show them what percentage of the questions they got right.


print("Quiz Time!\n")

#Question 1
answer1 = input("In what year did CCVI first open? ")
if answer1 == "1967": #checks if the answer is 1967 then says if its correct other wise it says says its false 
    print("Correct!\n")
    correct1 = 1#if the answer is correct then this variable becomes true. this is so the program can calculate how correct you were
else:
    print("Nope!\n")
    correct1 = 0#if the answer is false then this variable becomes false. this is so the program can calculate how correct you were

#Question 2
answer2 = input("What is 2^10? ")
if answer2 == "1024": #checks if the answer is 1024 then says if its correct other wise it says says its false 
    print("Correct!\n")
    correct2 = 1#if the answer is correct then this variable becomes true. this is so the program can calculate how correct you were
else:
    print("Nope!\n")
    correct2 = 0#if the answer is false then this variable becomes false. this is so the program can calculate how correct you were

#Question 3
print("Who sings \'Ramble On\' and \'Dyer Maker\'?") #simply prints question and multiple choice
print("A. Bon Jovi")
print("B. Led Zeppelin")
print("C. Anne Murray")
print("D. Metallica")
answer3 = input() #input line for answer
if answer3 == ("b" or "B"): #checks if the answer is capital B or lowercase b then says if your answer was correct other wise it says its false 
    print("Correct!\n")
    correct3 = 1 #if the answer is correct then this variable becomes true. this is so the program can calculate how correct you were
else:
    print("Nope!\n")
    correct3 = 0#if the answer is false then this variable becomes false. this is so the program can calculate how correct you were

#Question 4
print("Who created Python?") #simply prints question and multiple choice
print("A. James Gosling")
print("B. Ada Lovelace")
print("C. Grace Hopper")
print("D. Guido van Rossum")
answer4 = input() #input line for answer
if answer4 == ("d" or "D"): #checks if the answer is capital D or lowercase D then says if your answer was correct other wise it says its false 
    print("Correct!\n")
    correct4 = 1#if the answer is correct then this variable becomes true. this is so the program can calculate how correct you were
else:
    print("Nope!\n")
    correct4 = 0#if the answer is false then this variable becomes false. this is so the program can calculate how correct you were

#Question 5
que5 = correct1 + correct2 + correct3 + correct4
que5 = str(que5)
answer5 = input("How many questions have you gotten right on this quiz? ")
if answer5 == que5:
    print("Correct!\n")
    correct5 = 1#if the answer is correct then this variable becomes true. this is so the program can calculate how correct you were
else:
    print("Nope!\n")
    correct5 = 0#if the answer is false then this variable becomes false. this is so the program can calculate how correct you were


tot_correct = str(correct1 + correct2 + correct3 + correct4 + correct5)#adds up the trues and falses as a number of how many questions were correct. this becomes a string so it can be put in a string otherwise it wouldnt work
print("Congratulations, you got "+tot_correct+" answers right.")
tot_correct = int(tot_correct)
percentage = (tot_correct / 5) * 100 #calculates percentage by divding the amount correct by the total amount of questions
percentage = str(percentage) #convert to string so it can be put in a string otherwise it wouldnt work
print("That is a score of "+percentage+" percent")