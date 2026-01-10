import pygame
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()
fps = 60
flying = False
game_over = False
running = True
ground_scroll = 0
scroll_speed = 4
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()-pipe_frequency
pass_pipe = False
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"lesson 3/images/bird{i}.png")
            # image = pygame.transform.scale(image,(50,40))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.click = False
        

    def update(self):
        if flying == True:
            self.vel+=0.5
            if self.vel>8:
                self.vel = 8
            if self.rect.bottom<700:
                self.rect.y+=int(self.vel)
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            self.counter+=1
            flap_cooldown = 5
            if self.counter>flap_cooldown:
                self.counter = 0
                self.index+=1
                if self.index>= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        self.image = pygame.image.load("lesson 3/images/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        elif pos == -1:
            self.rect.topleft = [x,y+int(pipe_gap/2)]
    def update(self):
       self.rect.x-=scroll_speed
       if self.rect.right<0:
           self.kill()

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action = True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
bird = Bird(70,int(900/2))
bird_group.add(bird)
restart = pygame.image.load("lesson 3/images/restart button.png")
button = Button(900//2-50,900//2-100,restart)
screen = pygame.display.set_mode((900,900))
bg = pygame.image.load("lesson 3/images/flappybg.png")
ground = pygame.image.load("lesson 3/images/ground.png")


while running:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(ground_scroll,700))
    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()
    if flying == True and game_over == False:
        time_now = pygame.time.get_ticks()
        if time_now-last_pipe>pipe_frequency:
            pipe_height = random.randint(-100,100)
            b_pipe = Pipe(900,int(900/2)+pipe_height,-1)
            t_pipe = Pipe(900,int(900/2)+pipe_height,1)
            pipe_group.add_internal(t_pipe)
            pipe_group.add_internal(b_pipe)
            last_pipe = time_now
        pipe_group.update()
        ground_scroll-=scroll_speed
        if abs(ground_scroll)>30:
            ground_scroll = 0

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.blit(restart,(450,350))
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True


    pygame.display.update()
    

pygame.quit()