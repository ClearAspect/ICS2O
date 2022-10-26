#Roan Mason
#, 2021
#

import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 1") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock()

BLACK = (0,0,0)

#IMPORTED PICS
img_1 = pygame.image.load("zzzpics (5).png")
img_2 = pygame.image.load("zzzpics (30).png")
img_3 = pygame.image.load("zzzpics (64).png")

displayed_img = img_1

while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = pygame.mouse.get_pressed()
            
            screen.fill(BLACK) #clear screen
            
            if buttons[0]: #left mouse button
                displayed_img = img_1
            elif buttons[1]: #middle mouse button
                displayed_img = img_2
            elif buttons[2]: #right mouse button
                displayed_img = img_3
    
    screen.blit(displayed_img, [300,180])
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()