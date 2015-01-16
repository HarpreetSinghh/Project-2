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
pixMove = 3
offset = 10
 
movement = 'right'
fpsTime = pygame.time.Clock()
 
class RobotSprite:
 
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pirate.gif')
        self.rect = self.image.get_rect()
 
class TreasureChest:
  def __init__(self,image):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("treasure - Copy.gif")
    self.rect = self.image.get_rect()

class TresureFound:
 def__init__(self,text):
  pygame.sprite.Sprite.__init__(self
  
  #class and search to be completed
 
 
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Treasure Found!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = setDisplay.get_rect().centerx
textrect.centery = setDisplay.get_rect().centery
  
setDisplay.fill((255, 255, 255))
setDisplay.blit(text, textrect)
 
  
pygame.display.update()
 
 
def down(imgx,imgy):
    if movement == 'down':
        imgy += pixMove
        if bg.get_at((imgx,imgy+ offset)).g is not 0:
            if bg.get_at((imgx + offset,imgy )).g is not 0:
                left(imgx,imgy)
            elif bg.get_at((imgx - offset,imgy )).g is not 0:
                right(imgx,imgy)
def right(imgx,imgy):
    if movement == 'right':
        imgx += pixMove
        if bg.get_at((imgx + offset,imgy)).g is not 0:
            if bg.get_at((imgx,imgy + offset)).g is not 0:
                up(imgx,imgy)
            elif bg.get_at((imgx,imgy - offset)).g is not 0:
                down(imgx,imgy)
def up(imgx,imgy):
    if movement == 'up':
        imgy -= pixMove
        if bg.get_at((imgx,imgy - offset)).g is not 0:
            if bg.get_at((imgx + offset,imgy )).g is not 0:
                left(imgx,imgy)
            elif bg.get_at((imgx - offset,imgy )).g is not 0:
                right(imgx,imgy)
def left(imgx,imgy):
    if movement == 'left':
        imgx -= pixMove
        if bg.get_at((imgx,imgy+ offset)).g is not 0:
            if bg.get_at((imgx,imgy + offset)).g is not 0:
                up(imgx,imgy)
            elif bg.get_at((imgx,imgy - offset)).g is not 0:
                down(imgx,imgy)
                
while True:
 right(imgx,imgy)
 print movement , imgx,imgy 
    
 
 
    setDisplay.blit(bg, (0,0))
    setDisplay.blit(img, (imgx,imgy))
    setDisplay.blit(treasure, (115,100))
 
    pygame.display.flip()
 
 
     
    pygame.display.update()
    fpsTime.tick(FPS)
     
 
pygame.display.update()
