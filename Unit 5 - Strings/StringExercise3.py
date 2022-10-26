#Roan Mason
#May 20, 2021
#Ask the user to enter a word. Cut it into two "equal" parts. If the length of the word is odd, place the center character in the first half, so that the first half contains one more character than the second. Now print a new word with the first and second halves interchanged (second half first and the first half second)

s = input("Enter a word: ")

length = len(s)
odd = length % 2
pos1 = 0
pos2 = 0

first = ""
end = ""

if odd == 1:
    pos = ((length - 1) / 2) + 1
else:
    pos = length / 2

first = s[:int(pos)]
end = s[int(pos):int(length)]

print(end + first)