import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))
running = True

bg = pygame.image.load("images/background.png")
rocket = pygame.image.load("images/spaceship.png")

y = 250
x = 250


moves = {"up":False , "left":False, "right":False}

while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(rocket, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moves["up"] = True
            if event.key == pygame.K_LEFT:
                moves["left"] = True
            if event.key == pygame.K_RIGHT:
                moves["right"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moves["up"] = False

            if event.key == pygame.K_LEFT:
                moves["left"] = False

            if event.key == pygame.K_RIGHT:
                moves["right"] = False

    if moves["up"]:
        y-=4
    
    if moves["left"]:
        x-=4
        
    if moves["right"]:
        x+=4

    y+=2
    pygame.display.update()

    