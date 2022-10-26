#Roan Mason
#June 1, 2021
#Animation Exercises

import pygame

pygame.init() #start pygame
pygame.display.set_caption("Exercise Set #2") #window title
size = (700,500) #resoloution of window
screen = pygame.display.set_mode(size) #screen variable

clock = pygame.time.Clock()

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
CLOUD_COLOUR = (255,255,255)

cloud_x_pos = 0 #cloud starting  position
cloud_x_change = 1 #cloud speed

cloud_2_x_pos = 0 #cloud starting  position
cloud_2_x_change = 3 #cloud speed

gecko_x_pos = 0 #gecko starting  position
gecko_x_change = 3 #gecko speed
gecko_y_pos = 400 #gecko starting  position
gecko_y_change = 3#gecko speed

car_x_pos = 0 #car starting  position
car_x_change = 5 #car speed

#IMPORTED IMAGES (also resized)

gecko = pygame.image.load('gecko.png')
gecko = pygame.transform.scale(gecko, (50,50))

car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (143,43))

done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #check if user is trying to quit
            done = True        
    
    if cloud_x_pos > 700: #if the cloud reaches the right side 
        cloud_x_pos = -100 #reset the cloud position
    cloud_x_pos = cloud_x_pos + cloud_x_change #moves the cloud    
    
    if cloud_2_x_pos > 700: #if the cloud reaches the right side
            cloud_2_x_pos = -100 #reset the cloud position
    cloud_2_x_pos = cloud_2_x_pos + cloud_2_x_change #moves the cloud    
    
    
    if abs(cloud_x_pos - cloud_2_x_pos) < 70: #if the 2 clouds get close enough
        CLOUD_COLOUR = LIGHT_GREY #theyre touching (make grey)
    else: #they dont touch (make white)
        CLOUD_COLOUR = WHITE
    
    if gecko_x_pos >= 670 or gecko_x_pos <= -10: #if the gecko reaches a side
        gecko_x_change = gecko_x_change * -1 #reverse the way its going
    gecko_x_pos = gecko_x_pos + gecko_x_change #moves the gecko
    
    if gecko_y_pos >= 470 or gecko_y_pos <= 290: #if the gecko reaches a top or bottom
        gecko_y_change = gecko_y_change * -1 #reverse the way its going
    gecko_y_pos = gecko_y_pos + gecko_y_change #moves the gecko    
    
    if car_x_pos > 700: #if the car reaches the right side 
        car_x_pos = -100 #reset the cars position
    car_x_pos = car_x_pos + car_x_change #moves the cloud    
    
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
    
    #clouds
    
    #big cloud
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_x_pos,90,90,50])
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_x_pos,80,50,20])
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_x_pos+20,70,80,30])
    
    #small cloud
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_2_x_pos,90,60,35])
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_2_x_pos,75,50,30])
    pygame.draw.ellipse(screen, CLOUD_COLOUR, [cloud_2_x_pos-15,65,50,25])


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
    
    screen.blit(gecko, [gecko_x_pos,gecko_y_pos]) #add the gecko to the scene
    screen.blit(car, [car_x_pos,450]) #add the car to the scene
    
    
    pygame.display.flip() #display the drawings
    clock.tick(60) #FPS (Frames Per Second)
    
pygame.quit()