import pygame
class Spaceship:
    def __init__(self,image,angle):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(60,60))
        self.image = pygame.transform.rotate(self.image,angle)


pygame.init()

screen = pygame.display.set_mode((1000,600))
bg = pygame.image.load("lesson 3/images/space.png")
bg = pygame.transform.scale(bg,(1000,600))
red_spaceship = Spaceship("lesson 3/images/spaceship_red.png",(90))
yellow_spaceship = Spaceship("lesson 3/images/spaceship_yellow.png",(-90))

running = True

while running:
    screen.blit(bg,(0,0))
    screen.blit(red_spaceship.image,(100,100))
    screen.blit(yellow_spaceship.image,(800,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break


    pygame.display.update()