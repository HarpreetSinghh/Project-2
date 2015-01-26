basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Treasure Found!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = setDisplay.get_rect().centerx
textrect.centery = setDisplay.get_rect().centery
