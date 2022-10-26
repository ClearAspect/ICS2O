#Roan Mason
#June 1, 2021
#Ask the user to enter some text. If there are more than 3 ‘t’s then remove the first ‘t’ in the text. If there are 3 or less ‘t’s then remove the last ‘t’ in the text. If there are no ‘t’s at all then just output the text unchanged. Make your program loop so that the user can enter text more than once. The user will enter ‘q’ when they want to stop. 


done = False #used to make sure program starts

s = "" #Input String place holder
ts = "" #"t's" in the string place holder


first_t = "" #first "t" location
last_t = "" #last "t" location

new_s = "" #new string output


while not done: #as long as the player isnt finished (done = False)
    s = input("Enter some text (q to quit): ") #ask the user for a string
    ts = s.count("t") #count the number of "t's"
    
    if s == "q" or s == "Q": #if the user inputs q or Q than change done to True so the game ends
        done = True
        print("Goodbye!")
    elif ts == 0: #if there are no "t's" than just print what the user wrote
        print(s)    
    elif ts > 3: #if the number of "t's" is above 3 
        first_t = s.find("t") #find the first occurrence of "t"
        new_s = s[: first_t] + s[first_t + 1 :] #build a new string by cutting the string into 2 parts. 1: begining to the letter before the first "t" 2: The letter after "t" to the ending
        print(new_s) #print the new string
        
    elif ts <= 3:
        last_t = s.rfind("t") #find the last occurrence of "t" 
        new_s = s[: last_t] + s[last_t + 1 :]#build a new string by cutting the string into 2 parts. 1: begining to the letter before the last "t" 2: The letter after "t" to the ending
        print(new_s) #print the new string

