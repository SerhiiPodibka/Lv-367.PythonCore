
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE=(255,255,255)
PI=3.14
done = False
x=50
y=50
width=40
height=60
vol=5

while not done:
    for event in pygame.event.get(100): 
        if event.type == pygame.QUIT:
            done=True
     
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x=x-vol
    if keys[pygame.K_RIGHT]:
        x=x+vol
    if keys[pygame.K_UP]:
        y=y-vol
    if keys[pygame.K_DOWN]:
        y=y+vol
    #pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    #pygame.draw.rect(screen, (64, 128, 255), (150, 20, 100, 75), 8)
    
    #pygame.draw.line(screen, WHITE, [10,30], [290,15],3)
    #pygame.draw.line(screen, WHITE, [10,50], [290,35])
    #pygame.draw.aaline(screen, WHITE, [10,70], [290,55])

    #pygame.draw.ellipse(screen, WHITE, (10,50,280,100))
    #pygame.draw.circle(screen, WHITE, (100,100),50)
    #pygame.draw.circle(screen, WHITE, (200,100),50,10)

    #pygame.draw.arc(screen, WHITE, (10,50,280,100),0,PI)
    #pygame.draw.arc(screen, WHITE, (50,30,200,150),PI,2*PI,3)
    
    #pygame.draw.polygon(screen, WHITE,[[150,10],[180,50],[90,90],[30,30],8] )
    gameDisplay.fill((0,0,0))

    pygame.draw.rect(screen, (255,0,0), [x,y,width,height])

    pygame.display.update()