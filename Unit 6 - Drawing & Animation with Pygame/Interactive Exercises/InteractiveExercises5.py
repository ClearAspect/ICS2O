#Roan Mason
#June 3, 2021
#Write a program where the screen is divided into two equal sides.  Pressing the arrow keys on the keyboard should change the colour of the corresponding side, as described in the table here (sample run on next page):


import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 5") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock() #create the fps clock
 
#colours
RED = (255,0,0)
ORANGE = (255,127,0)
GREEN = (0,255,0)
PURPLE = (255,0,255)
BLACK = (0,0,0)
LEFT_COLOUR = (255,0,0)
RIGHT_COLOUR = (255,127,0)

while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
        if event.type == pygame.KEYDOWN: #Check for Key pushes
            if event.key == pygame.K_LEFT: #if its the left arrow
                LEFT_COLOUR = RED #change right side to red
            if event.key == pygame.K_RIGHT: #if its the right arrow
                LEFT_COLOUR = GREEN #change left side to green
            if event.key == pygame.K_UP: #if its the up arrow
                RIGHT_COLOUR = ORANGE #change right side to orange
            if event.key == pygame.K_DOWN: #if its the down arrow
                RIGHT_COLOUR = PURPLE #change right side to purple
    
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, LEFT_COLOUR, [0,0,350,500])
    pygame.draw.rect(screen, RIGHT_COLOUR, [350,0,350,500])
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()