#Roan Mason
#May 31, 2021
#Drawing Exercises part 1

import pygame

pygame.init()
pygame.display.set_caption("Exercise Set #1") #Exercise 1
size = (800,600) #Exercise 1
screen = pygame.display.set_mode(size)
RED = (255,0,0) #Exercise 2
GREEN = (0,255,0) #Exercise 3
BLUE = (0,0,255) #Exercise 3
PURPLE = (255,0,255) #Exercise 3
YELLOW = (255,255,0) #Exercise 4
BLACK = (0,0,0) #Exercise 4
ORANGE = (255,127,0) #Exercise 5
WHITE = (255,255,255) #Exercise 6

pygame.draw.rect(screen, RED, [0,0,100,100]) #Exercise 2
pygame.draw.rect(screen, GREEN, [700,0,100,100]) #Exercise 3
pygame.draw.rect(screen, BLUE, [0,500,100,100]) #Exercise 3
pygame.draw.rect(screen, PURPLE, [700,500,100,100]) #Exercise 3

for x in range(100,700,50):  #Exercise 4
    pygame.draw.rect(screen, YELLOW, [x,0,50,100])  #Exercise 4
    pygame.draw.rect(screen, BLACK, [x,0,50,100],2)  #Exercise 4

for x in range(100,500,50): #Exercise 5
    pygame.draw.rect(screen, ORANGE, [0,x,100,50])  #Exercise 5
    pygame.draw.rect(screen, BLACK, [0,x,100,50],2) #Exercise 5
    pygame.draw.rect(screen, ORANGE, [700,x,100,50]) #Exercise 5
    pygame.draw.rect(screen, BLACK, [700,x,100,50],2) #Exercise 5

for y in range(100,500,25): #Exercise 5
    for x in range(100,700,25): #Exercise 5
        pygame.draw.rect(screen, WHITE, [x,y,25,25]) #Exercise 5
        pygame.draw.rect(screen, BLACK, [x,y,25,25],2) #Exercise 5
    

pygame.display.flip() #Exercise 2
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()