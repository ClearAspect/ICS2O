#Roan Mason
#June 14, 2021
#Shooter Game
'''
Enhancements
- Use animated images for characters (walking / running / jumping, etc)
- Save multiple high scores to a data file and display them in order

- Use a timer
- Save 1 high score to a data file

- Include nice-looking graphics (png files are good for this)
- Use a custom pygame program icon (not the snake)
- Use lists to help make your program
- Use functions to help make your program



Credits:

Duck Sprites
https://www.spriters-resource.com/nes/duckhunt/sheet/13056/
Some Sounds from
https://www.sounds-resource.com/nes/duckhunt/sound/4233/
'''

import pygame
import random
from spritesheet import Spritesheet
import pickle
import time

done = False
pygame.init() #start pygame
pygame.display.set_caption("Duck Shooter") #window title
icon = pygame.image.load('icon.png') #icon load
pygame.display.set_icon(icon) #set window icon
size = (800,600) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock()

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)


#Game Variables
gamestate = "menu" #is the game in play mode or is it in a menu?
pos = pygame.mouse.get_pos() #find the mouse position
m_x = pos[0] #create the x coordinate
m_y = pos[1] #create the y coordinate

misses = 0
kills = 0
round = 1
round_delay = 0 #timed delay between rounds

#high score and score variable
#==========================================================================
score = 0 #the score
#load the highscores
highscores = pickle.load(open("Highscores.dat", "rb")) #read the High Score data file to get the high scores
#==========================================================================



#import images from spritesheet
my_spritesheet = Spritesheet('duck_spritesheet.png') #tell python what image is the spritesheet

#lists for each different type of duck and there different animation positions from the sprite sheet
#==========================================================================


duck_1_ = [my_spritesheet.parse_sprite('duck_1_1.png'), my_spritesheet.parse_sprite('duck_1_2.png'), my_spritesheet.parse_sprite('duck_1_3.png'), my_spritesheet.parse_sprite('duck_1_4.png'), my_spritesheet.parse_sprite('duck_1_5.png'), my_spritesheet.parse_sprite('duck_1_6.png'), my_spritesheet.parse_sprite('duck_1_7.png'), my_spritesheet.parse_sprite('duck_1_8.png'), my_spritesheet.parse_sprite('duck_1_9.png')]

r_duck_1_ = [my_spritesheet.parse_sprite('r_duck_1_1.png'), my_spritesheet.parse_sprite('r_duck_1_2.png'), my_spritesheet.parse_sprite('r_duck_1_3.png'), my_spritesheet.parse_sprite('r_duck_1_4.png'), my_spritesheet.parse_sprite('r_duck_1_5.png'), my_spritesheet.parse_sprite('r_duck_1_6.png'), my_spritesheet.parse_sprite('r_duck_1_7.png'), my_spritesheet.parse_sprite('r_duck_1_8.png'), my_spritesheet.parse_sprite('r_duck_1_9.png')]



duck_2_ = [my_spritesheet.parse_sprite('duck_2_1.png'), my_spritesheet.parse_sprite('duck_2_2.png'), my_spritesheet.parse_sprite('duck_2_3.png'), my_spritesheet.parse_sprite('duck_2_4.png'), my_spritesheet.parse_sprite('duck_2_5.png'), my_spritesheet.parse_sprite('duck_2_6.png'), my_spritesheet.parse_sprite('duck_2_7.png'), my_spritesheet.parse_sprite('duck_2_8.png'), my_spritesheet.parse_sprite('duck_2_9.png')]

r_duck_2_ = [my_spritesheet.parse_sprite('r_duck_2_1.png'), my_spritesheet.parse_sprite('r_duck_2_2.png'), my_spritesheet.parse_sprite('r_duck_2_3.png'), my_spritesheet.parse_sprite('r_duck_2_4.png'), my_spritesheet.parse_sprite('r_duck_2_5.png'), my_spritesheet.parse_sprite('r_duck_2_6.png'), my_spritesheet.parse_sprite('r_duck_2_7.png'), my_spritesheet.parse_sprite('r_duck_2_8.png'), my_spritesheet.parse_sprite('r_duck_2_9.png')]



duck_3_ = [my_spritesheet.parse_sprite('duck_3_1.png'), my_spritesheet.parse_sprite('duck_3_2.png'), my_spritesheet.parse_sprite('duck_3_3.png'), my_spritesheet.parse_sprite('duck_3_4.png'), my_spritesheet.parse_sprite('duck_3_5.png'), my_spritesheet.parse_sprite('duck_3_6.png'), my_spritesheet.parse_sprite('duck_3_7.png'), my_spritesheet.parse_sprite('duck_3_8.png'), my_spritesheet.parse_sprite('duck_3_9.png')]

r_duck_3_ = [my_spritesheet.parse_sprite('r_duck_3_1.png'), my_spritesheet.parse_sprite('r_duck_3_2.png'), my_spritesheet.parse_sprite('r_duck_3_3.png'), my_spritesheet.parse_sprite('r_duck_3_4.png'), my_spritesheet.parse_sprite('r_duck_3_5.png'), my_spritesheet.parse_sprite('r_duck_3_6.png'), my_spritesheet.parse_sprite('r_duck_3_7.png'), my_spritesheet.parse_sprite('r_duck_3_8.png'), my_spritesheet.parse_sprite('r_duck_3_9.png')]

#==========================================================================


#variable for what iteration of animation the duck is(more than one because more than one duck might be on the screen)
#==========================================================================

#variable to count what frame the game is on
ani_count = 0

#following comments apply to all
duck_1_death_counter = 0 #counts the ticks before changing death animation frames 
duck_1_fly = 0 #what is the starting frame from the fly animation
duck_1_glide = 3 #what is the starting frame for the gliding animation
duck_1_ani = 0 #counts the ticks before changing flying/gliding animation frames


duck_2_death_counter = 0
duck_2_fly = 0
duck_2_glide = 3
duck_2_ani = 0


duck_3_death_counter = 0
duck_3_fly = 0
duck_3_glide = 3
duck_3_ani = 0


#duck postion change variables and start pos variables

#following comments apply to all

#Random speeds of Duck
duck1_x_change = -random.randint(5,6) 
duck1_y_change = -random.randint(4,6)
#Starting position
duck1_x = 180
duck1_y = 350
duck1_hit = False #was the duck shot?
duck1_miss = True #miss detection

duck2_x_change = -random.randint(4,6)
duck2_y_change = -random.randint(4,6)
duck2_x = 375
duck2_y = 300
duck2_hit = False
duck2_miss = True

duck3_x_change = -random.randint(4,7)
duck3_y_change = -random.randint(4,7)
duck3_x = 725
duck3_y = 300
duck3_hit = False
duck3_miss = True
#==========================================================================



#Imported images and/or change their size
title = pygame.image.load('title.png')
title = pygame.transform.scale(title,(524,232))
backround = pygame.image.load('backround.png') #import image
backround = pygame.transform.scale(backround,(800,600)) #convert size
cursor = pygame.image.load('cursor.png') #import image
cursor = pygame.transform.scale(cursor,(50,50)) #convert size
round_sprite = pygame.image.load('round_sprite.png') #import image
round_sprite = pygame.transform.scale(round_sprite,(220,50)) #convert size
score_sprite = pygame.image.load('score_sprite.png') #import image
score_sprite = pygame.transform.scale(score_sprite,(217,93)) #convert size
hits_and_misses = pygame.image.load('hits_and_misses.png') #import image
hits_and_misses = pygame.transform.scale(hits_and_misses,(397,50))

tree2_1 = pygame.image.load('tree2-1.png') #import image
tree2_1 = pygame.transform.scale(tree2_1, (117,210)) #convert size
tree2_2 = pygame.image.load('tree2-2.png') #import image
tree2_2 = pygame.transform.scale(tree2_2, (117,210)) #convert size

#Custom Fonts for game
font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
font2 = pygame.font.Font('ARCADECLASSIC.TTF', 48)
font3 = pygame.font.Font('ARCADECLASSIC.TTF', 25)
font4 = pygame.font.Font('ARCADECLASSIC.TTF', 75)

#Imported Sounds
wing_flap = pygame.mixer.Sound('wing_flap.wav')
gun_shot = pygame.mixer.Sound('gun_shot.wav')
game_over = pygame.mixer.Sound('game_over.wav')
theme_sound = pygame.mixer.Sound('theme_sound.wav')


#Handle Events (key presses, clicks etc)
#==========================================================================
while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
        if event.type == pygame.KEYDOWN:
            if gamestate == "menu":
                if event.key == pygame.K_SPACE:
                    gamestate = "game"
                    theme_sound.play()
                    time.sleep(1)
            if gamestate == "gameover":
                if event.key == pygame.K_SPACE:
                    gamestate = "menu"                
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = pygame.mouse.get_pressed()
            if buttons[0] and gamestate == "game": #left mouse button
                if (m_x > duck1_x and m_x < (duck1_x + 65)) and (m_y > duck1_y and m_y < (duck1_y + 50)): #has duck one been shot?
                    duck1_hit = True #tell the game that the duck was shot
                    duck1_miss = False
                    gun_shot.play()
                    misses = 0
                    score += 25 * round #add to score
                if (m_x > duck2_x and m_x < (duck2_x + 65)) and (m_y > duck2_y and m_y < (duck2_y + 50)): #has duck two been shot?
                    duck2_hit = True #tell the game that the duck was shot
                    duck2_miss = False
                    gun_shot.play()
                    misses = 0
                    score += 50 * round #add to score
                if (m_x > duck3_x and m_x < (duck3_x + 65)) and (m_y > duck3_y and m_y < (duck3_y + 50)): #has duck three been shot?
                    duck3_hit = True #tell the game that the duck was shot
                    duck3_miss = False
                    gun_shot.play()
                    misses = 0
                    score += 100 * round #add to score
            if (buttons[0] and gamestate == "game") and (duck1_miss == True and duck2_miss == True and duck3_miss == True):
                misses += 1
                gun_shot.play()
    
    #Game Reset after Loss
    #==========================================================================
    if gamestate == "game":
        if misses == 4: #if you get 4 misses than its game over and the game resets 
            time.sleep(.5)
            game_over.play()
            
            misses = 0
            gamestate = "gameover"
            
            #RESET EVERY VARIABLE TO RESTART GAME
            
            misses = 0
            kills = 0
            round = 1
            round_delay = 0           
            ani_count = 0
            
            duck_1_death_counter = 0
            duck_1_fly = 0 
            duck_1_glide = 3 
            duck_1_ani = 0
            
            
            duck_2_death_counter = 0
            duck_2_fly = 0
            duck_2_glide = 3
            duck_2_ani = 0
            
            
            duck_3_death_counter = 0
            duck_3_fly = 0
            duck_3_glide = 3
            duck_3_ani = 0

            duck1_x_change = -random.randint(5,6) 
            duck1_y_change = -random.randint(4,6)
            #Starting position
            duck1_x = 180
            duck1_y = 350
            duck1_hit = False
            duck1_miss = True
            
            duck2_x_change = -random.randint(4,6)
            duck2_y_change = -random.randint(4,6)
            duck2_x = 375
            duck2_y = 300
            duck2_hit = False
            duck2_miss = True
            
            duck3_x_change = -random.randint(4,7)
            duck3_y_change = -random.randint(4,7)
            duck3_x = 725
            duck3_y = 300
            duck3_hit = False
            duck3_miss = True            
            
            
    
#==========================================================================    
    screen.fill(BLACK)
    
    
    if gamestate == "menu": #if youre on the main menu
        #Main Screen Text and Objects
        score = 0 #reset score after game reset 
        
        #create text to diplay
        instruct = font.render("press  space  to  start", False, WHITE)
        signature  = font3.render("Deve loped by  Roan Mason", False, WHITE)
        
        #High scores in the game
        s_highscore  = font3.render("High Scores", False, WHITE)
        highscore1  = font3.render("1      " + str(highscores[0]), False, WHITE)
        highscore2  = font3.render("2      " + str(highscores[1]), False, WHITE)
        highscore3  = font3.render("3      " + str(highscores[2]), False, WHITE)
        #pygame.draw.line(screen, GREEN, (400,0),(400,600)) #just to see middle of screen for text alignment
        
        #display images/text
        screen.blit(signature, [170,280])
        screen.blit(s_highscore, [20,300])
        screen.blit(highscore1, [20,330])
        screen.blit(highscore2, [20,360])
        screen.blit(highscore3, [20,390])
        screen.blit(title, [138,50])
        screen.blit(instruct, [145,500])
    
    elif gamestate == "game": #If youre on the Game screen
         
        ani_count += 1 #animation counter(goes up every tick)
        
        
        #DUCK Animation Handler
        #DUCK positioning and AI
        #==========================================================================
        duck1_x += duck1_x_change
        duck1_y += duck1_y_change
        
        duck2_x += duck2_x_change
        duck2_y += duck2_y_change        
        
        duck3_x += duck3_x_change
        duck3_y += duck3_y_change
        
        
        
        if kills == (11 + round):
            round += 1
            round_delay += 1
            kills = 0
    
        #Duck ONE Animation Movement and Event Handler
        #==========================================================================

        
        #Most comments made on this bird apply to all 

        if duck1_y > 600: #When the bird falls off screen
            #random speed of the bird
            duck1_x_change = -random.randint(5,6) 
            duck1_y_change = -random.randint(4,6)
            #respawn the bird in its original position
            duck1_x = 180
            duck1_y = 350
            duck1_hit = False #disable the detection of a hit
            kills += 1
            duck_1_death_counter = 0 #reset the Death animation counter so other if statements dont occur 
        elif duck_1_death_counter == 60: #if a second passes update the animiation
            duck_1_ani = 7 #set the duck to the death frame
            duck1_y_change = 6 #make the duck fall downwards
        elif duck1_hit == True: #if the duck is shot
            #stop the ducks movement
            duck1_miss = True #tell the game that it is now possible to miss
            duck1_x_change = 0 
            duck1_y_change = 0
            duck_1_ani = 6 #set the duck to the death frame
            duck_1_death_counter += 1 #add to the timer
        
            
        else: #if the duck hasnt been shot
            if (duck1_y_change < 0 or duck1_y_change > 0) and ani_count == 7: #if the duck is moving vertically play the vertical flying animation
                    duck_1_ani = duck_1_fly
                    duck_1_fly += 1
                    if duck_1_fly == 3 and ani_count == 7: #if the last animation frame is plated reset it
                        duck_1_fly = 0
                        wing_flap.play()
            elif duck1_y_change == 0 and ani_count == 7:
                duck_1_ani = duck_1_glide
                duck_1_glide += 1
                if duck_1_glide == 6 and ani_count == 7:
                    duck_1_glide = 3
                    wing_flap.play()
            

            if duck1_y <= 150: #if the bird hits 150 that it will coast/glide
                duck1_y_change = 0
            if duck1_x <= 0 or duck1_x > 740: #if the bird hits the sides then it will bounce
                duck1_x_change = -duck1_x_change
        #==========================================================================
        #Duck Two Animation Movement and Event Handler
        #==========================================================================
        
        
        if duck2_y > 600:
            duck2_x_change = -random.randint(4,6)
            duck2_y_change = -random.randint(4,6)
            duck2_x = 375
            duck2_y = 300
            duck2_hit = False
            kills += 1
            duck_2_death_counter = 0        
        elif duck_2_death_counter == 60: 
            duck_2_ani = 7 
            duck2_y_change = 6
        elif duck2_hit == True:
            duck2_miss = True
            duck2_x_change = 0
            duck2_y_change = 0
            duck_2_ani = 6 
            duck_2_death_counter += 1
        else:
            
            if (duck2_y_change < 0 or duck2_y_change > 0) and ani_count == 7:
                duck_2_ani = duck_2_fly
                duck_2_fly += 1
                if duck_2_fly == 3 and ani_count == 7:
                    duck_2_fly = 0
                    wing_flap.play()
            elif duck2_y_change == 0 and ani_count == 7:
                duck_2_ani = duck_2_glide
                duck_2_glide += 1
                if duck_2_glide == 6 and ani_count == 7:
                    duck_2_glide = 3
                    wing_flap.play()

            if duck2_y <= 90 and duck2_x > 300 and duck2_x < 450: #if duck 2 is in the 300-450 range on x and at 90 y than stop the y movment
                duck2_y_change = 0
            elif duck2_y >= 350 or duck2_y <= 0: #if the bird hits the top or bottom of the screen than it will bounce
                duck2_y_change = -duck2_y_change
            if duck2_x <= 0 or duck2_x > 740: #if the bird hits the sides then it will bounce
                duck2_x_change = -duck2_x_change
                if duck2_x > 100 and duck2_x < 200: #if the bird goes between 100-200 x it will speed up vertically
                    duck2_y_change = 6
        #==========================================================================
        #Duck Three Animation Movement and Event Handler
        #==========================================================================
        
        
        if duck3_y > 600:
            duck3_x_change = -random.randint(4,7)
            duck3_y_change = -random.randint(4,7)
            duck3_x = 725
            duck3_y = 300
            duck3_hit = False
            kills += 1
            duck_3_death_counter = 0        
        elif duck_3_death_counter == 60: 
            duck_3_ani = 7 
            duck3_y_change = 6
        elif duck3_hit == True:
            duck3_miss = True
            duck3_x_change = 0
            duck3_y_change = 0
            duck_3_ani = 6 
            duck_3_death_counter += 1
        else:
            
            if (duck3_y_change < 0 or duck3_y_change > 0) and ani_count == 7:
                duck_3_ani = duck_3_fly
                duck_3_fly += 1
                if duck_3_fly == 3 and ani_count == 7:
                    duck_3_fly = 0
                    wing_flap.play()
            elif duck3_y_change == 0 and ani_count == 7:
                duck_3_ani = duck_3_glide
                duck_3_glide += 1
                if duck_3_glide == 6 and ani_count == 7:
                    duck_3_glide = 3
                    wing_flap.play()
            
            
            if duck3_y >= 350 or duck3_y <= 0: #if the bird hits the top or bottom of the screen than it will bounce
                duck3_y_change = -duck3_y_change
            if duck3_x <= 0 or duck3_x > 740: #if the bird hits the sides then it will bounce
                duck3_x_change = -duck3_x_change
        #==========================================================================
            
        if ani_count == 7:
            ani_count = 0
        #==========================================================================
    
    
        screen.blit(backround, [0,0]) #display the backround
        
        #HUD
        screen.blit(round_sprite, [10,480])
        screen.blit(score_sprite, [573,453])
        screen.blit(hits_and_misses, [201,525])
        
        #score
        score2 = score
        score2 = str(score2)
        score2 = font2.render(score2, False, WHITE)
        screen.blit(score2, [590,454])
        
        #hits and misses
        kills2 = kills
        kills2 = str(kills)
        kills2 = font2.render(kills2, False, WHITE)
        screen.blit(kills2, [322,526])
        
        misses2 = misses
        misses2 = str(misses2)
        misses2 = font2.render(misses2, False, WHITE)
        screen.blit(misses2, [558,526])
        
        #round
        round2 = round
        round2 = str(round2)
        round2 = font2.render(round2, False, WHITE)
        screen.blit(round2, [164,481])
        
        #Display the ducks and change the way they face depending on the direction of movement
        
        if duck1_x_change < 0: #if the duck is moving left. use the left facing sprites
            screen.blit(r_duck_1_[duck_1_ani], (duck1_x, duck1_y))
        else: #otherwise dont
            screen.blit(duck_1_[duck_1_ani], (duck1_x, duck1_y))
        
        if duck2_x_change < 0: #if the duck is moving left. use the left facing sprites
            screen.blit(r_duck_2_[duck_2_ani], (duck2_x, duck2_y))
        else: #otherwise dont
            screen.blit(duck_2_[duck_2_ani], (duck2_x, duck2_y))
        
        if duck3_x_change < 0: #if the duck is moving left. use the left facing sprites
            screen.blit(r_duck_3_[duck_3_ani], (duck3_x, duck3_y))
        else: #otherwise dont
            screen.blit(duck_3_[duck_3_ani], (duck3_x, duck3_y))
        
        #Trees
        screen.blit(tree2_1, [150,250])
        screen.blit(tree2_1, [700,200])
        screen.blit(tree2_1, [350,210])
        screen.blit(tree2_2, [-50,200])
        
        
        
        #Cursor capture and target display
        pos = pygame.mouse.get_pos() #find the mouse position
        m_x = pos[0] #create the x coordinate
        m_y = pos[1] #create the y coordinate        
        screen.blit(cursor, [m_x - 25, m_y - 25])        
        
    #Gameover Screen and Highscore calculation
    #==========================================================================
    elif gamestate == "gameover":
        
        gameover = font4.render("GAME OVER", False, WHITE)
        screen.blit(gameover, [225,150])
        
        s_score = font.render("you had a score of", False, WHITE)
        screen.blit(s_score, [200,350])
        
        score2 = score
        score2 = str(score2)        
        score2 = font.render(score2, False, WHITE)
        score2_rect = score2.get_rect(center=(800/2, 420))
        screen.blit(score2, score2_rect)        
        
        instruct = font.render("press  space  to  continue", False, WHITE)
        screen.blit(instruct, [115,500])
        
        
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)

#highscores = [0, 0, 0]
#pickle.dump(highscores, open("Highscores.dat", "wb"))
if score > highscores[0]: #if you highscore is bigger than number one then move down all the numbers and replace it
    highscores[2] = highscores[1]
    highscores[1] = highscores[0]
    highscores[0] = score
elif score > highscores[1]: #if you highscore is bigger than number two then move down all the numbers under it and replace it
    highscores[2] = highscores[1]
    highscores[1] = score    
elif score > highscores[2]: #if you highscore is bigger than number three then replace it
    highscores[2] = score
        
pickle.dump(highscores, open("Highscores.dat", "wb")) #store the new scores in a Data file

pygame.quit()