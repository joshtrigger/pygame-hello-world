import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
run = True
background = (255, 255, 255)
font = pygame.font.SysFont('Myriad Pro', 48, 1, 1)
text = font.render('Hello', 1, (0, 0, 255), (255, 255, 255))
clock = pygame.time.Clock()
text_size = text.get_size()

while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_position = pygame.mouse.get_pos()
    x, y = mouse_position

    screen.fill(background)
    pygame.display.set_caption('Game')

    if x+text_size[0] > 800:
        x = 800-text_size[0]

    if y+text_size[1] > 600:
        y = 600-text_size[1]

    screen.blit(text, (x, y))
    pygame.display.update()


pygame.quit()
