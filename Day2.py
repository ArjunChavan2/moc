#Day 2: Animation

import pygame

pygame.init()
width, height = 1000, 750
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("My Game")

x = 100
y = 100
size_x = 70
size_y = 50

dvd = pygame.image.load("dvd.png")
dvd = pygame.transform.scale(dvd,(size_x,size_y))

goRight, goDown = True, True


while True:
  screen.fill((5,0,10))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(dvd,(x,y))
  if(goRight):
    if(x >= width - size_x):
      goRight = False
    else:
      x += 10
  else:
    if(x <= 0):
      goRight = True
    else:
      x-= 10

  if(goDown):
    if(y >= height - size_y):
      goDown = False
    else:
      y += 10
  else:
    if(y <= 0):
      goDown = True
    else:
      y-= 10
      
  pygame.display.update()
  clock.tick(30)