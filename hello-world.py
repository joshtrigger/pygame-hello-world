import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('Myriad Pro', 48, 1, 1)
text = font.render('Hello World', 1, (0, 0, 255), (255, 255, 255))
textSize = text.get_size()
x = 0
dirX = 1
clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    screen.blit(text, (x, 30))
    x += 5*dirX

    if x + textSize[0] > 800 or x <= 0:
        dirX *= -1

    pygame.display.update()
