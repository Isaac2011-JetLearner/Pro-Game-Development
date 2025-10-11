import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))

bee = pygame.image.load("images/bee.png")
bg = pygame.image.load("images/grassbackground.png")
flower = pygame.image.load("images/flower.png")

running = True
x = 300
y = 450

x_1 = random.randint(10,590)
y_1 = 10

up = False
left = False
right = False
down = False

while running:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(bee,(x,y))
    screen.blit(flower,(x_1,y_1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False


    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
              down = True
    if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
              down = False

    if up:
        y-=4
    
    if left:
        x-=4
        
    if right:
        x+=4

    if down:
         y+=4
         
    y_1+=3

    pygame.display.update()