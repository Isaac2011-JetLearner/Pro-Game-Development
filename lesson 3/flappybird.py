import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
fps = 60
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            image = pygame.image.load(f"lesson 3/images/bird{i}.png")
            image = pygame.transform.scale(image,(50,40))
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))
        self.vel = 0
        self.click = False
        

    def Update(self):
        if flying == True:
            self.vel+=0.5
            if self.vel>8:
                self.vel = 8
            if self.rect.bottom<700:
                self.rect.y+=int(self.vel)
        
        self.counter+=1
        flap_cooldown = 5
        if self.counter>flap_cooldown:
            self.counter = 0
            self.index+=1
            if self.index>= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
bird = Bird(70,int(900/2))
bird_group.add(bird)
flying = False
game_over = False
screen = pygame.display.set_mode((900,700))
bg = pygame.image.load("lesson 3/images/flappybg.png")
bg = pygame.transform.scale(bg,(900,500))
ground = pygame.image.load("lesson 3/images/ground.png")
ground = pygame.transform.scale(ground,(900,200))
restart = pygame.image.load("lesson 3/images/restart button.png")
restart = pygame.transform.scale(restart,(100,100))
running = True
ground_scroll = 0
scroll_speed = 4


while running:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(ground_scroll,500))
    bird_group.draw(screen)
    bird_group.update()
    ground_scroll-=scroll_speed
    if abs(ground_scroll)>30:
        ground_scroll = 0

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.blit(restart,(450,350))


    pygame.display.update()
    

pygame.init()