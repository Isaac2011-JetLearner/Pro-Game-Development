import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))
running = True

bg = pygame.image.load("images/background.png")
rocket = pygame.image.load("images/spaceship.png")

y = 250
up = False
while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(rocket, (250,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False

    if up:
        y-=4
        
    y+=2
    pygame.display.update()

    