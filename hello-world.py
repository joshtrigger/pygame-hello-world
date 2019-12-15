import pygame,sys
from pygame.locals import * 

pygame.init()

screen = pygame.display.set_mode((800, 600))
run=True
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
backgroud=yellow

while run:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run = False;
    elif event.type == KEYDOWN and event.key == K_b:
      backgroud=blue
    elif event.type == KEYDOWN and event.key == K_r:
      backgroud=red
    
    pygame.display.set_caption('Snake Game')
    screen.fill(backgroud)
    pygame.display.update()

pygame.quit()