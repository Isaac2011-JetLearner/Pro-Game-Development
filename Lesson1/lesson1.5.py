import pygame 
import random

pygame.init()

class Circle:
    def __init__(self,color,radius):
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen,self.color,(250,250),self.radius)

    def grow(self):
        self.radius+=10

    def change_color(self):
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

        

screen = pygame.display.set_mode((500,500))

running = True
blue_circle = Circle("red",100)
rect_1 = pygame.Rect((250,240),(100,200))

while running:
    pygame.draw.rect(screen,"blue",rect_1)
    blue_circle.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            blue_circle.grow()
            blue_circle.change_color()
    pygame.display.update()
pygame.quit()

