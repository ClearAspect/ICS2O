#Roan Mason
#June 4, 2021
#Drawing and Animation Test - Programming Question


import pygame


pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Unit 7 Test - Roan Mason")

SKYBLUE = (61,206,255)
GREEN = (0,255,0)
DARK_GREEN = (22,130,16)
BROWN = (153,102,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)


clock = pygame.time.Clock()

sun_x = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    screen.fill(SKYBLUE)
    pygame.draw.rect(screen, GREEN, [0,300,700,200])
    pygame.draw.ellipse(screen, YELLOW, [sun_x,50,85,85])
    sun_x += 1
    
    if sun_x >= 700:
        sun_x = -100
    
    
    for x in range(20,700,20):
        for y in range(300,500,60):
            pygame.draw.line(screen, DARK_GREEN, [x,y], [x,y+40],2)
    
    pygame.draw.rect(screen, BROWN, [500,220,30,100])
    pygame.draw.ellipse(screen, DARK_GREEN, [460,140,110,130])
    
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    
    pygame.draw.polygon(screen, WHITE, [[x,y], [x+50,y-25], [x+25,y], [x+50,y+25]])
    
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()