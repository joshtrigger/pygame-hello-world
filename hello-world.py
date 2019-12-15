import pygame,sys

pygame.init()

screen = pygame.display.set_mode((800,600))

font=pygame.font.SysFont('Myriad Pro', 48,1,1)

text=font.render('Hello World', 1, (0,0,255),(255,255,255))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  screen.blit(text,(30,30))
  pygame.display.update()