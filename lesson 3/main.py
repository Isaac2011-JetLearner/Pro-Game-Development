import pygame
class Spaceship:
    def __init__(self,image,angle,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(60,60))
        self.image = pygame.transform.rotate(self.image,angle)
        self.move = {"up":False,"down":False}
        self.bullets = []
    
    def handle_movement(self):
        if self.move["up"]:
            self.y-=4
        elif self.move["down"]:
            self.y+=4

class Bullet:
    def __init__(self,color,x,y):
        self.x = x
        self.y = y
        self.color = color

pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

bg = pygame.image.load("lesson 3/images/space.png")
bg = pygame.transform.scale(bg,(1000,600))
red_spaceship = Spaceship("lesson 3/images/spaceship_red.png",(90),100,100)
yellow_spaceship = Spaceship("lesson 3/images/spaceship_yellow.png",(-90),800,100)

running = True
move = {"up": False, "down": False}
while running:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(red_spaceship.image,(red_spaceship.x,red_spaceship.y))
    screen.blit(yellow_spaceship.image,(yellow_spaceship.x,yellow_spaceship.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                red_spaceship.move["up"] = True
            if event.key == pygame.K_DOWN:
                red_spaceship.move["down"] = True

            if event.key == pygame.K_SPACE:
                red_spaceship_bullet = Bullet("red",20,20)
                red_spaceship.bullets.append(red_spaceship_bullet)
            

            if event.key == pygame.K_w:
                yellow_spaceship.move["up"] = True
            if event.key == pygame.K_s:
                yellow_spaceship.move["down"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
               red_spaceship.move["up"] = False
            if event.key == pygame.K_w:
                yellow_spaceship.move["up"] = False

            if event.key == pygame.K_UP:
               red_spaceship.move["down"] = False

            if event.key == pygame.K_s:
               yellow_spaceship.move["down"] = False


    red_spaceship.handle_movement()
    yellow_spaceship.handle_movement()
    pygame.display.update()


print(red_spaceship.bullets)