import pygame
import sys
import time
from pygame.locals import *
 
pygame.init()
 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
 
setDisplay = pygame.display.set_mode((1181,781))
title = pygame.display.set_caption("Treasure Hunt")
 
bg = pygame.image.load("map.gif")
img = pygame.image.load('pirate.gif')
treasure = pygame.image.load('treasure.gif')
FPS = 30
imgx = 7
imgy = 519
pixMove = 5
 
movement = 'right'
 
fpsTime = pygame.time.Clock()
 
class RobotSprite:
 
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pirate.gif')
        self.rect = self.image.get_rect()
 
 
 
 
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Treasure Found!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = setDisplay.get_rect().centerx
textrect.centery = setDisplay.get_rect().centery
  
setDisplay.fill((255, 255, 255))
setDisplay.blit(text, textrect)
 
  
pygame.display.update()
 
 
 
while True:
 
    if movement == 'right':
        imgx += pixMove
        if imgx > 116:
            movement = 'up'
 
    elif movement == 'up':
        imgy -= pixMove
         
         
     
    setDisplay.blit(img, (imgx,imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    setDisplay.blit(bg, (0,0))
    setDisplay.blit(img, (imgx,imgy))
    setDisplay.blit(treasure, (115,100))
 
    pygame.display.flip()
 
 
     
    pygame.display.update()
    fpsTime.tick(FPS)
     
 
pygame.display.update()
