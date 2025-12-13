import pygame
import random
pygame.font.init()
screen = pygame.display.set_mode((600,600))
font = pygame.font.SysFont("Arial",25)
class Gamecard:
    def __init__(self,image,name,x,y):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.name = name
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.text = font.render(self.name,1,"Blue")

    def draw(self):
         screen.blit(self.image,(self.x,self.y))

    


clock = pygame.time.Clock()
bg = pygame.image.load("lesson 3/images/grassbackground.png")
bg = pygame.transform.scale(bg,(1200,700))

nba2k = Gamecard("lesson 3/images/nba2K26.png","nba2k",100,100)
roblox = Gamecard("lesson 3/images/roblox.png","roblox",100,250)
fortnite = Gamecard("lesson 3/images/fortnite.png","fornite",100,400)


games = [nba2k,roblox,fortnite]

games2 = games[:]
random.shuffle(games2)
running = True

start = []
end = []
while running:
    screen.blit(bg,(0,0))
    for game in games:
         game.draw()

    y = 150
    for game in games2:
         screen.blit(game.text,(350,y))
         y+=150
         

    

    clock.tick(60)
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

    for i in range(len(end)):
         pygame.draw.circle(screen,"red",start[i],15)
         pygame.draw.circle(screen,"red",end[i],15)
         pygame.draw.line(screen,"red",start[i],end[i])

    pygame.display.update()















pygame.init()