#Roan Mason
#June 1, 2021
#Drawing Exercises part 2 - Draw a Scene

import pygame

pygame.init() #start pygame
pygame.display.set_caption("Exercise Set #2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable

#Colours
DARK_RED = (127,0,0)
RED = (255,0,0)
ORANGE = (255,127,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
L_BLUE = (0,127,255)
BLUE = (0,0,255)
VIOLET = (255,0,255)
PURPLE = (127,0,255)
BROWN = (127,64,0)
LIGHT_BROWN = (150,75,0)
BLACK = (0,0,0)
LIGHT_GREY = (192,192,192)
DARK_GREY = (40,40,40)
WHITE = (255,255,255)

#Exercise 1
screen.fill(L_BLUE) #the sky
pygame.draw.circle(screen, YELLOW, [0,0],75) #the circle of the sun 
pygame.draw.line(screen, YELLOW, [0,0],[100,12],6) #sun ray
pygame.draw.line(screen, YELLOW, [0,0],[95,45],6) #sun ray
pygame.draw.line(screen, YELLOW, [0,0],[80,80],6) #sun ray
pygame.draw.line(screen, YELLOW, [0,0],[45,95],6) #sun ray
pygame.draw.line(screen, YELLOW, [0,0],[12,100],6) #sun ray

#rainbow
pygame.draw.ellipse(screen, RED, [175,50,700,600], 10)
pygame.draw.ellipse(screen, ORANGE, [182,57,686,586], 10)
pygame.draw.ellipse(screen, YELLOW, [189,64,672,572], 10)
pygame.draw.ellipse(screen, GREEN, [196,71,658,558], 10)
pygame.draw.ellipse(screen, BLUE, [203,78,644,544], 10)
pygame.draw.ellipse(screen, PURPLE, [210,85,633,533], 10)
pygame.draw.ellipse(screen, VIOLET, [217,92,616,516], 10)

pygame.draw.rect(screen, BROWN, [0,200,700,300]) #ground
pygame.draw.ellipse(screen, BLUE, [330,200,260,70]) #water
pygame.draw.ellipse(screen, WHITE, [350,210,80,40], 1) #ripple
pygame.draw.ellipse(screen, WHITE, [355,215,65,30], 1) #ripple
pygame.draw.ellipse(screen, WHITE, [360,217,50,25], 1) #ripple
pygame.draw.ellipse(screen, WHITE, [375,223,15,10], 1) #ripple
pygame.draw.rect(screen, DARK_RED, [445,160,230,110]) #house walls
pygame.draw.polygon(screen, LIGHT_BROWN, [[560,120],[445,160],[675,160]])
pygame.draw.rect(screen, LIGHT_BROWN, [595,210,20,20]) #window
pygame.draw.rect(screen, LIGHT_BROWN, [620,210,20,20]) #window
pygame.draw.rect(screen, LIGHT_BROWN, [595,235,20,20]) #window
pygame.draw.rect(screen, LIGHT_BROWN, [620,235,20,20]) #window
pygame.draw.rect(screen, LIGHT_BROWN, [470,210,40,60]) #door
pygame.draw.ellipse(screen, BLACK, [503,240,5,5]) #door knob
pygame.draw.rect(screen, DARK_GREY, [0,300,700,300]) #Road
for x in range(0,700,44): #sidewalk
    pygame.draw.rect(screen, LIGHT_GREY, [x,300,44,44])
    pygame.draw.rect(screen, DARK_GREY, [x,300,44,44],1)
for x in range(0,700,90): #road lines
    pygame.draw.rect(screen, WHITE, [x,427,50,5])

pygame.display.flip() #display the drawings
#check if user tries to quit the game

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()