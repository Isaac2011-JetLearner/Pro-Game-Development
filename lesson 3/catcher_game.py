import pygame
import random
pygame.font.init()
score = 0
font = pygame.font.SysFont("Alasassy Caps",20)
white = (255,255,255)
screen = pygame.display.set_mode((1000,800))
bg = pygame.image.load("lesson 3/images/grassbackground.png")
bg = pygame.transform.scale(bg,(1000,800))
class Holder():
    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(200,150))
        self.rect = self.image.get_rect(center = (self.x,self.y))
        
    def draw(self):
         screen.blit(self.image,self.rect)
    
    def detect_colision(self):
            global score
            if catcher.rect.colliderect(cash.rect):
                print("YES")
                score+=1
            
            if catcher.rect.colliderect(leaf.rect) or catcher.rect.colliderect(rocks.rect):
                score-=1

                



items = ["lesson 3/images/cash.png","lesson 3/images/leaf.png","lesson 3/images/rocks.png"]
class Things():
    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def draw(self):
        screen.blit(self.image,self.rect)



cash = Things(items[0],random.randint(2,999),5)
rocks = Things(items[2],random.randint(2,997),5)
leaf = Things(items[1],random.randint(2,994),5)
charcaters = []



catcher = Holder("lesson 3/images/pen_catcher.png",400,600)
left = False
right = False
running = True
while running:
   
    screen.blit(bg,(0,0))
    catcher.draw()
    leaf.draw()
    cash.draw()
    rocks.draw()
    score_text = font.render(f"score: {score}",1,white)
    screen.blit(score_text, (10,10))

    leaf.y+=2
    cash.y+=2
    rocks.y+=2

    if cash.y>810:
        cash.x = random.randint(2,999)
        cash.y=5
        cash.y+=0.25
    
    elif rocks.y>810:
        rocks.x =random.randint(2,997)
        rocks.y=5
        rocks.y+=0.2
    
    elif leaf.y>810:
        leaf.x = random.randint(2,994)
        leaf.y=5
        leaf.y+=0.2

    if catcher.x<=0:
        catcher.x=0

    elif catcher.x>=800:
        catcher.x=800

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                right = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False



    if left:
        catcher.x-=3
        
    if right:
        catcher.x+=3

    catcher.detect_colision()
    pygame.display.update()

        
print(score)

pygame.quit()