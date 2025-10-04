import pygame 
pygame.init()


class Rectangle:
    def __init__(self,width,color,rect_1):
        self.width = width
        self.rect_1 = rect_1 
        self.color = color

    
    def draw(self):
        pygame.draw.rect(screen,self.color,((self.rect_1)),self.width)


screen = pygame.display.set_mode((500,500))
running = True


blue_rect = Rectangle(200,"blue",((300,100),(250,100)))

while running:
    blue_rect.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
pygame.quit()
