import pygame
import math
import sys
from pygame.locals import *;
from sys import exit
pygame.init()


blk = pygame.Color(0,0,0)
BG = ('BG.png')
pygame.init()
screen = pygame.display.set_mode((800, 600))
B_G = pygame.image.load(BG).convert_alpha()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
fpsclock = pygame.time.Clock()



class Shork(pygame.sprite.Sprite):


 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.image.load('SHORK.png')
  screen = pygame.display.get_surface()
  self.x = 62
  self.y = 50
  self.direction = "down"

 def Moving(self):

  if self.direction == "right":
   self.x += 1
  elif self.direction == "left":
   self.x -= 1
  elif self.direction == "down":
   self.y += 1
  elif self.direction == "up":
   self.y -= 1


 def Path(self):

  if self.x == 62 and self.y == 538:
   self.direction = "right"

  if self.x == 246 and self.y == 538:
   self.direction = "up"

  if self.x == 246 and self.y == 366:
   self.direction = "left"

  if self.x == 176 and self.y == 366:
   self.direction = "up"

  if self.x == 176 and self.y == 114:
   self.direction = "right"

  if self.x == 530 and self.y == 114:
   self.direction = "down"

  if self.x == 530 and self.y == 366:
   self.direction = "left"

  if self.x == 460 and self.y == 366:
   self.direction = "down"

  if self.x == 460 and self.y == 538:
   self.direction = "right"

  if self.x == 644 and self.y == 538:
   self.direction = "up"
  if self.y == 0:
   sys.exit()

Shork = Shork()

Run = True


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("test1")
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print("test3")
    while Run:
      fpsclock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
    screen.fill((0,0,0))
    Shork.Moving() 
    Shork.Path()
    angle = 360-math.atan2(Shork.y-200,Shork.x-300)*180/math.pi
    rotimage = pygame.transform.rotate(B_G, angle)
    screen.blit(Shork.image, (Shork.x, Shork.y))
    pygame.display.update()
    rect = rotimage.get_rect(center=(300,200))
    screen.blit(rotimage,rect)
    pygame.display.update()