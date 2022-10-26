#Roan Mason
#May 20, 2021
#Ask the user to enter two words separated by a space. Print the words out in reverse order

s = input("Enter two words with a space between them:\n")
space = s.find(' ')
start = s[0:space]
end = s[space + 1:]

print(end+" "+start)