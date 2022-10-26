#Roan Mason
#, 2021
#

import pygame

done = False
pygame.init() #start pygame
pygame.display.set_caption("Interactive Exercise 2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable
clock = pygame.time.Clock()


ORANGE = (255,127,0)
BLUE = (0,0,255)

#circle starting point
x = 325
y = 225

#all false so circle doesnt move unless user says so
up = False
left = False
down = False
right = False

while not done:
    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True
        if event.type == pygame.KEYDOWN: #if a key is pressed down 
            #check if its WASD, if so allow movement based on the key w = up a = left etc.
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_d:
                right = True
        if event.type == pygame.KEYUP: #if a key is released
            #check if its WASD, if so stop movement based on the key w = up a = left etc.
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_d:
                right = False
           
    if up == True: #if up is true then the circles y coordinate is subtracted by one so it visualy goes up. this is the same for the rest of the values
        y -= 3
    if left == True:
        x -= 3
    if down == True:
        y += 3
    if right == True:
        x += 3
    
    screen.fill(ORANGE)
    pygame.draw.ellipse(screen, BLUE, [x,y,50,50])
    
    
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
pygame.quit()