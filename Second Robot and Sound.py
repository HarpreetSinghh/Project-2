import pygame
import sys
import time
import random
from pygame.locals import *
import pygame.mixer

 
pygame.init()
 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

green = (  0, 255,   0)
 
setDisplay = pygame.display.set_mode((1181,981))
title = pygame.display.set_caption("Treasure Hunt")
sound = pygame.mixer.Sound('song.wav') 
bg = pygame.image.load("map1.gif")
img = pygame.image.load('pirate.gif')
img1 = pygame.image.load('pirate1.gif')
treasure = pygame.image.load('treasure.gif')
FPS = 30
imgx = 7
imgy = 519
img1x=1160
img1y=160
pixMove = 5
offset = 30  
movement = 'right'
movement1 = 'left'

light = 'red'
light = 'green'
light1 = 'red'
light1 = 'green'
 
fpsTime = pygame.time.Clock()
 
class Robot:
 
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pirate.gif')
        self.rect = self.image.get_rect()

    
    def checking_right1(img1x,img1y,movement1):
        if bg.get_at((img1x + offset,img1y)).g is not  0:
            if bg.get_at((img1x,img1y + offset)).g is  0:
                movement1 = 'down'
            elif bg.get_at((img1x,img1y - offset)).g is  0:
                movement1 = 'up'
        return movement1 

    def checking_left1(img1x,img1y,movement1):
        if bg.get_at((img1x - offset,img1y)).g is not  0:
                if bg.get_at((img1x ,img1y + 100)).g is  0:
                    movement1 = 'down'
                elif bg.get_at((img1x,img1y - offset )).g is  0:
                    movement1 = 'up'
        return movement1

    def checking_down1(img1x,img1y,movement1):
        if bg.get_at((img1x,img1y + offset)).g is not  0:
                if bg.get_at((img1x + offset,img1y)).g is  0:
                    movement1 = 'right'
                elif bg.get_at((img1x - offset,img1y )).g is  0:
                    movement1 = 'left'
        return movement1

    def checking_up1(img1x,img1y,movement1):
        if bg.get_at((img1x,img1y - offset)).g is not  0:
                if bg.get_at((img1x - offset,img1y )).g is  0:
                    movement1 = 'left'
                elif bg.get_at((img1x + offset,img1y )).g is  0:
                    movement1 = 'right'
        return movement1
    def checking_treasure(imgx,imgy):
        if imgx>975 and imgy==519:
            setDisplay.blit(treasure, (0,0))

    while True:
            sound.play()

            if movement1 == 'left':
                img1x -= pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_left1(img1x,img1y,movement1)

                
            elif movement1 == 'down':
                img1y += pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_down1(img1x,img1y,movement1)

            elif movement1 == 'right':
                img1x += pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_right1(img1x,img1y,movement1)
                


            elif movement1 == 'up':
                img1y -= pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_up1(img1x,img1y,movement1)



            setDisplay.blit(bg, (0,0))
            setDisplay.blit(img, (imgx,imgy))
            setDisplay.blit(treasure, (982,518))
            setDisplay.blit(img1, (img1x,img1y))
            pygame.display.flip()
     
 
     
            pygame.display.update()
            fpsTime.tick(FPS)
