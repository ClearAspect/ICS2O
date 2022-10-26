#Roan Mason
#May 21, 2021
#Loop Assignment Game. https://docs.google.com/document/d/1c3Xiea3lXHAu8t1Ev7thwvm6Mmbclqz7PQQMa7WAXgg/edit

#The basic idea behind Homeward Bound is to help Nova on her journey home through the forest while being chased by a group of hungry wolves. You’ll need to manage her hunger, energy level, and how far ahead of the hungry wolves she is. In order to win the game, Nova needs to make it home without being caught by the wolves (or starving, or passing out from exhaustion).

import random

#start game
done = False

#setups for regular variables in game
action = "" #empty input line
dis_travelled = 0 #total distance travelled
hunger = 0 #hunger stat
hunger_refill = 3 #number of snacks
stamina = 0 #fatigue/tiredness
enemy_dis = 20 #number of km away from wolves

#setups for random variables
rand_wolves = 0 #random wolf movement
rand_mod_speed = 0 #random moderate speed
rand_gal_speed = 0 #random gallop speed
snack_shack = 0 #chance for snack shack

#intro line (Title and description)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n| Welcome to Homeward Bound!  |\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
print("Nova the brave little dog is lost in the forest and and she needs your help to get home.\nThere are hungry wolves nearby! Survive your journey home and outrun the wolves.\n")

#Actual Game
while not done:
    print("\nNova is",(200 - dis_travelled),"kilometers from home.") #200km - distance travelled is the amount left to travel
    #game action options
    print("A. Eat a snack")
    print("B. Run at moderate speed")
    print("C. Gallop at full speed")
    print("D. Stop and rest")
    print("E. Status check")
    print("Q. Quit")
    action = input("Your Choice? ") #for use to input their decision
    if action == "Q" or action == "q": #if the user inputs q the game quits
        done = True
    if action == "A" or action == "a": #if the user inputs a:
        hunger -= hunger #hunger is reset
        hunger_refill -= 1 #snacks are reduced by one
        rand_wolves = random.randint(7,14) #random number of kilometers the wolves will travel
        enemy_dis -= rand_wolves #the wolves total distance away is the current distance - how much they moved towards you
        print("\nNova feels much better!\n")
    if action == "B" or action == "b": #if the user inputs b:
        rand_mod_speed = random.randint(5,12) #random number of kilometers the nova will travel at moderate speed
        dis_travelled += rand_mod_speed #total distance travelled by nova is the current distance plus what she just ran
        hunger += 1 #add hunger for running
        stamina += 1 #add fatigue for running
        rand_wolves = random.randint(7,14) #random number of kilometers the wolves will travel
        enemy_dis = (enemy_dis - rand_wolves) + rand_mod_speed #the wolves total distance away is the current distance - how much they moved towards you, and then the amount you moved away from them
        snack_chack = random.randint(1,20) #add the chance of finding a snack shack while running around
        if snack_shack == 20: #if you find the snack shack:
            hunger_refill = 3 #snacks are restored
            stamina -= stamina #stamina is reset
            hunger -= hunger #hunger is reset
            print("Nova found a secret snack shack in the forest!/nShe has a full compliment of snacks and eats her fill while she rests.")
        print("\nNova travelled",rand_mod_speed,"kilometers\n")
    if action == "C" or action == "c": #if the user inputs c: 
        rand_gal_speed = random.randint(10,20) #random number of kilometers the nova will travel at gallop speed
        dis_travelled += rand_gal_speed #total distance travelled by nova is the current distance plus what she just ran
        hunger += 1 #add hunger for running
        stamina += random.randint(1,3) #add random fatigue for running at a faster speed
        rand_wolves = random.randint(7,14) #random number of kilometers the wolves will travel
        enemy_dis = (enemy_dis - rand_wolves) + rand_gal_speed #the wolves total distance away is the current distance - how much they moved towards you, and then the amount you moved away from them
        snack_chack = random.randint(1,20) #add the chance of finding a snack shack while running around
        if snack_shack == 20: #if you find the snack shack:
            hunger_refill = 3 #snacks are restored
            stamina -= stamina #stamina is reset
            hunger -= hunger #hunger is reset
            print("Nova found a secret snack shack in the forest!/nShe has a full compliment of snacks and eats her fill while she rests.")        
        print("\nNova travelled",rand_gal_speed,"kilometers\n")
    if action == "D" or action == "d": #if the user inputs d:
        stamina -= stamina #reset stamina 
        rand_wolves = random.randint(7,14) #random number of kilometers the wolves will travel
        enemy_dis -= rand_wolves #the wolves total distance away is the current distance - how much they moved towards you
        print("\nNova feels refreshed, but the wolves sounds closer...\n")
    if action == "E" or action == "e": #if the user inputs e:
        print("\nKilometers travelled:",dis_travelled) #says how far youve travelled
        print("Snacks left:",hunger_refill) #says how many snacks are left
        print("The wolves are",enemy_dis,"kilometers behind you") #says how far away the wolves are
    if hunger == 5 or hunger == 6: #if your hungers gets to 5 or 6 you are warned of losing the game
        print("Nova's getting really hungry...") 
    if hunger >= 7: #if your hunger gets to 7 or above you lose and the game resets
        print("Nova passed out from hunger")
        done = True
    if stamina == 6 or stamina == 7 or stamina == 8: #if your stamina gets to 5 or 6 you are warned of losing the game
        print("Nova's getting really tired...")
    if stamina >= 9: #if your stamina reaches 9 or above you lose and the game resets
        print("Nova has passed out from exhaustion")
        done = True
    if enemy_dis <= 15 and enemy_dis >= 1: #if the wolves get within 15km of you a message is displayed warning you of their pressence
        print("The wolves are getting close!")
    if enemy_dis <= 0: #if the wolves catch up to you you lose
        print("Nova was caught by the wolves...")
        done = True
    if dis_travelled >= 200: #if you travel the full 200km without losing you win the game and nova makes it home.
        print("Nova made it all the way home and escaped the wolves!")
        print("~~~~~~~You win!!!!!~~~~~~~~","\n","         __","\n","        /  \ ","\n","       / ..|\ ","\n","      (_\  |_)","\n","      /  \@' ","\n","_   /  `   |","\n","\\/  \  | _\ ","\n"," \   /_ || \_","\n","  \____)|_ ) \_)   ")
        done = True
    