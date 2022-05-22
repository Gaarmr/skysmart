import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
BG_COLOR = (50, 50, 50)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
screen.fill(BG_COLOR)

color=(0,0,0) #For retangle
my_rect = pygame.Rect((100, 20, 100, 400))
pygame.draw.rect(screen, color, my_rect, 1)

pygame.display.update()
print(pygame.display.set_mode())

# BG_COLOR = pygame.Color('grey12')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    clock.tick(60)
    pygame.display.flip()