#Roan Mason
#June 3, 2021
#Write a program that will display the coordinates of the mouse’s current position anywhere on the screen, dynamically changing over time as the user moves the mouse

import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock()


GREEN = (0,255,0)
BLACK = (0,0,0)

font = pygame.font.SysFont("Comic Sans", 40, False, True)
 
while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
    #now code
    screen.fill(BLACK)
    
    pos = pygame.mouse.get_pos() #find the mouse position
    x = pos[0] #create the x coordinate
    y = pos[1] #create the y coordinate
    text_img = font.render("X: " + str(x) + ", " + "Y: " + str(y), True, GREEN)
    screen.blit(text_img, [x,y])
    
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()