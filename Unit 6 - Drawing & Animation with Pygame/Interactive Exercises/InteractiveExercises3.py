#Roan Mason
#June 3, 2021
#Write a program where a 100px diameter blue circle is positioned in the centre of the screen.  When the mouse is hovered over the circle, the circle will turn red.

import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock() #create the fps clock

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
CIRCLE_COLOUR = BLUE

while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
    
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, CIRCLE_COLOUR, [300,200,100,100])
    
    pos = pygame.mouse.get_pos() #find the mouse position
    x = pos[0] #create the x coordinate
    y = pos[1] #create the y coordinate    
    
    if (x <= 400 and x >= 300) and (y <= 300 and y >= 200):
        CIRCLE_COLOUR = RED
    else:
        CIRCLE_COLOUR = BLUE
    
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()