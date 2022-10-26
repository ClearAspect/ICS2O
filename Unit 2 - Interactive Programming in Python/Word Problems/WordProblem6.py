#Roan Mason
#Apr, 26, 2021
#Kelly got a 95% in Math, a 98% in Programming, a 92% in Science, and a 88% in English. What was Kelly’s average grade?

math_mark = 0.95 * 100
programming_mark = 0.98 * 100
science_mark = 0.92 * 100
english_mark = 0.88 * 100
average_mark = ((math_mark + programming_mark + science_mark + english_mark) / 4)

print("Math","\t","\t","{0:.0f}%".format(math_mark))
print("Programming","\t","{0:.0f}%".format(programming_mark))
print("Science","\t","{0:.0f}%".format(science_mark))
print("English","\t","{0:.0f}%".format(english_mark))
print("Average:","\t","{0:.0f}%".format(average_mark))