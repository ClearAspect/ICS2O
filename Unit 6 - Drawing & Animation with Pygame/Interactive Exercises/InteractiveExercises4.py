#Roan Mason
#June 3, 2021
#Write a program where a 100px diameter orange circle is positioned in the centre of the screen.  When the user clicks on the circle with the right mouse button, the circle should turn purple. If the user right clicks anywhere else, the circle should change back to orange

import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock()

ORANGE = (255,127,0)
PURPLE = (255,0,255)
BLACK = (0,0,0)
CIRCLE_COLOUR = ORANGE

while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: #does the user push down on the mouse
            buttons = pygame.mouse.get_pressed() #variable for mouse being pushed
            if buttons[2]: #if the right mouse button is pushed
                if (x <= 400 and x >= 300) and (y <= 300 and y >= 200): #if the cursor is in the circles coordinates
                    CIRCLE_COLOUR = PURPLE
                else: #if its not in the circle
                    CIRCLE_COLOUR = ORANGE
                    
    pos = pygame.mouse.get_pos() #find the mouse position
    x = pos[0] #create the x coordinate
    y = pos[1] #create the y coordinate
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, CIRCLE_COLOUR, [300,200,100,100])


    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()