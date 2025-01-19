from turtledemo.sorting_animate import Block

import pygame
import random

from vv import screen

BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
PURPLE=(255,0,255)
YELLOW=(255,255,0)

class Block(pygame.sprite.Sprite):
    def__init__(self, color, width,height):
       super().__init__()

    self.image=pygame.Surface([width,height])
    self.image.fill(color)

    self.rect=self.image.get_rect()

 def update(salf):
     self.rect.y  +=1
     if self.rect.y>410:
         self.reset.pos()

         self.rect.x +=pos[0]
         self.rect.y +=pos[1]


pygame_width= 700
screen_height=400
screen=pygame.display.set_mode([screen_width])