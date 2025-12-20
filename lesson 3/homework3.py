import pygame
import random

screen = pygame.display.set_mode((600,600))

bg = pygame.image.load("lesson 3/images/whitebackground.png")
bg = pygame.transform.scale(bg,(600,600))

running = True

start = []
end = []

r = random.randint(0,255)
g= random.randint(0,255)
b = random.randint(0,255)

while running:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
             pos = pygame.mouse.get_pos()
             start.append(pos)

        if event.type == pygame.MOUSEBUTTONUP:
             pos = pygame.mouse.get_pos()
             end.append(pos)
             r = random.randint(0,255)
             g = random.randint(0,255)
             b = random.randint(0,255)

    for i in range(len(end)):
        pygame.draw.circle(screen,(r,g,b),start[i],15)
        pygame.draw.circle(screen,(g,b,r),end[i],15)
        pygame.draw.line(screen,(b,r,g),start[i],end[i])


    pygame.display.update()