import pygame
import random

class character():
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(90,90))
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.move = {"up":False,"down":False,"left":False,"right":False}

    def movement(self):
        if self.move["up"]:
            self.rect.y-=7
        elif self.move["down"]:
            self.rect.y+=7

        elif self.move["right"]:
            self.rect.x+=7

        elif self.move["left"]:
            self.rect.x-=7


pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

bg = pygame.image.load("lesson 3/images/space.png")
bg = pygame.transform.scale(bg,(1000,600))

avatar = character(500,500,"lesson 3/images/avatar.png")
water = character(random.randint(1,1000),10,"lesson 3/images/water.png")

running = True

while running:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(water.image,(water.rect.topleft))
    screen.blit(avatar.image,(avatar.rect.topleft))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                avatar.move["up"] = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                avatar.move["right"] = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                avatar.move["left"] = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                avatar.move["down"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                avatar.move["up"] = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                avatar.move["right"] = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                avatar.move["left"] = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                avatar.move["down"] = False


    water.rect.y+=5

    if water.rect.y>=600:
        water.rect.x = random.randint(1,1000)
        water.rect.y = 10

    score = 1
    if water.rect.colliderect(avatar.rect):
        water.rect.x = random.randint(1,1000)
        water.rect.y = 10
        score+=1
        print("WATERRR")
        print(score)

            
    avatar.movement()
    pygame.display.update()
