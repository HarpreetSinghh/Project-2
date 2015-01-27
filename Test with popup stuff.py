import pygame, sys, time
from pygame.locals import *

pygame.init()

#Set up window
pygame.event.set_grab(0)
pygame.mouse.set_visible(1)
screen = pygame.display.set_mode((300,200))
shape = screen.convert_alpha()
pygame.display.set_caption("Sniper Alert")

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

#Draw on surface object
screen.fill(BLACK)

def alert():
    #Create a font
    font = pygame.font.Font(None,50)

    #Render the text
    text = font.render("Game Over", True, RED)

    #Create a rectangle
    textRect = text.get_rect()

    #Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #Blit the text
    screen.blit(lol, textRect)
    pygame.display.update()
