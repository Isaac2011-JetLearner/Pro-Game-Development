import pygame
class UP:
    def __init__(self):
        pass

pygame.init()

screen = pygame.display.set_mode((1000,600))

bg = pygame.image.load("lesson 3/images/racebg.png")
bg = pygame.transform.scale(bg,(1000,600))

red_car = pygame.image.load("lesson 3/images/redcar.png")
red_car = pygame.transform.scale(red_car,(120,70))

green_car = pygame.image.load("lesson 3/images/greencar.png")
green_car = pygame.transform.scale(green_car,(120,70))

blue_car = pygame.image.load("lesson 3/images/greencar.png")
blue_car = pygame.transform.scale(blue_car,(120,70))


running = True

while running:
    screen.blit(bg,(0,0))
    screen.blit(red_car,(100,500))
    screen.blit(green_car,(300,500))
    screen.blit(blue_car,(500,500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
