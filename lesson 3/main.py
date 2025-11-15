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
        self.rect = self.image.get_rect(center = (self.x,self.y))
    
    def detect_colision(self,enemyship):
        for bullet in self.bullets:
            if bullet.rect.colliderect(enemyship.rect):
                self.bullets.remove(bullet)

    
    def handle_movement(self):
        if self.move["up"]:
            self.rect.y-=4
        elif self.move["down"]:
            self.rect.y+=4

        for bullet in self.bullets:
            if bullet.rect.x<=0 or bullet.rect.x>=1000:
                self.bullets.remove(bullet)
            else:
                bullet.fire()
                bullet.draw()
            


class Bullet:
    def __init__(self,color,center):
        self.x,self.y = center
        self.color = color
        self.rect = pygame.Rect(self.x,self.y, 10,10)

    def fire(self):
        if self.color == "red":
            self.rect.x+=5
        else:
            self.rect.x-=5

    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)



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
    screen.blit(red_spaceship.image,(red_spaceship.rect.topleft))
    screen.blit(yellow_spaceship.image,(yellow_spaceship.rect.topleft))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                red_spaceship.move["up"] = True
            if event.key == pygame.K_s:
                red_spaceship.move["down"] = True

            if event.key == pygame.K_a:
                red_spaceship_bullet = Bullet("red",red_spaceship.rect.center)
                red_spaceship.bullets.append(red_spaceship_bullet)

            if event.key == pygame.K_l:
                yellow_spaceship_bullet = Bullet("yellow",yellow_spaceship.rect.center)
                yellow_spaceship.bullets.append(yellow_spaceship_bullet)
            

            if event.key == pygame.K_UP:
                yellow_spaceship.move["up"] = True
            if event.key == pygame.K_DOWN:
                yellow_spaceship.move["down"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
               red_spaceship.move["up"] = False
            if event.key == pygame.K_UP:
                yellow_spaceship.move["up"] = False

            if event.key == pygame.K_s:
               red_spaceship.move["down"] = False

            if event.key == pygame.K_DOWN:
               yellow_spaceship.move["down"] = False


    red_spaceship.handle_movement()
    yellow_spaceship.handle_movement()
    red_spaceship.detect_colision(yellow_spaceship)
    yellow_spaceship.detect_colision(red_spaceship)
    pygame.display.update()


