#Roan Mason
#May 6, 2021
#You and your date are trying to get a table at a restaurant. The stylishness of your clothes is rated in the range from 0...10, as is the stylishness of your date's clothes. If either you or your date is very stylish (8 or more) then you will get a table. Unless of course one of you has a style of 2 or less, in which case you will definitely not get a table. Otherwise you might get a table. Ask the user for their stylishness level and their dates' stylishness level, and output whether they will get a table, might get a table, or will not get a table.


print("Welcome to the restaurant!")

style1 = int(input("What is your style rating(0-10)? "))
style2 = int(input("What is your date's style rating(0-10)? "))

if style1 <= 2 or style2 <= 2:
    print("Sorry, no table for you")
elif style1 >= 8 or style2 >= 8:
    print("We have a table right here for you")
else:
    print("Wait here, we might have a table for you...")