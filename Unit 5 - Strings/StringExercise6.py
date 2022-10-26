#Roan Mason
#May 20, 2021
#Some words are special. What makes a word special you ask? Special words have exactly the same number of vowels (a,e,i,o,u) and consonants (the other 21 letters in the alphabet). Ask the user to enter a word and output whether or not it is special.

#whats your word
s = input("Enter a word: ")

#find the length of the word and count if any vowels are contained in it
length = len(s)
vowela = s.count("a")
vowele = s.count("e")
voweli = s.count("i")
vowelo = s.count("o")
vowelu = s.count("u")
vowels = vowela + vowele + voweli + vowelo + vowelu #add the vowel counts up

#the amount of consonants is any letter besides vowels. remove the vowel count from the letter count to get the number of consonants
consonants = length - vowels

#if the amount of constants and vowels are the same its a special word
if consonants == vowels:
    print("That's a special word!") 
else: #if they are different its not.
    print("Your word is not special.")