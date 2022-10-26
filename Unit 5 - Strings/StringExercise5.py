#Roan Mason
#May 20, 2021
#Ask the user to enter their favourite animal. Print out the name of the animal, except double every character

word = input("What is your favourite animal? ")

s = ""

for letter in word:
    s += letter*2
print(s)
    