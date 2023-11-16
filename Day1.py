#Day 1: Basic Pygame + Movement
import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")


x = 100
y = 100
size = 50
while True:
  screen.fill((255,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x -= 10
      elif event.key == pygame.K_RIGHT:
        x += 10
      elif event.key == pygame.K_UP:
        y -= 10
      elif event.key == pygame.K_DOWN:
        y += 10
      elif event.key == pygame.K_SPACE:
        size += 10;
      elif event.key == pygame.K_BACKSPACE:
        size -= 10;
      elif event.key == pygame.K_1:
        x = y = 100;
        size = 50;

  pygame.draw.rect(screen, (0,255,0),(x,y,size,size))
  pygame.display.update()
  
