import pygame
import random
pygame.font.init()
font = pygame.font.SysFont("comic sans", 25)
class Recycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lesson 3/images/paperbag.png")
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect(center = (random.randint(10,1000),random.randint(10,700)))

class Non_recycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lesson 3/images/plastic.png")
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect(center = (random.randint(10,1000),random.randint(10,700)))

class Bin():
    def __init__(self):
        self.image = pygame.image.load("lesson 3/images/bin.png")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect(center = (0,0))



recycleable_group = pygame.sprite.Group()
non_recycleable_group = pygame.sprite.Group()
screen = pygame.display.set_mode((1000,700))
bg = pygame.image.load("lesson 3/images/space.png")
bin = Bin()
running = True
score = 0




for i in range(10):
    obj_2 = Non_recycleable()
    non_recycleable_group.add(obj_2)
    obj = Recycleable()
    recycleable_group.add(obj)


while running:
    score_text = font.render(f"score: {score}",1,"white")
    screen.blit(bg,(0,0))
    non_recycleable_group.draw(screen)
    recycleable_group.draw(screen)
    screen.blit(bin.image,bin.rect.center)
    screen.blit(score_text,(10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        bin.rect.x+=3

    elif keys[pygame.K_LEFT]:
        bin.rect.x-=3

    elif keys[pygame.K_UP]:
        bin.rect.y-=3

    elif keys[pygame.K_DOWN]:
        bin.rect.y+=3

    collided_obj_2 = pygame.sprite.spritecollide(bin,non_recycleable_group,1)
    collided_obj = pygame.sprite.spritecollide(bin,recycleable_group,1)
    score+=len(collided_obj)
    score-=len(collided_obj_2)
    pygame.display.update()





pygame.init()