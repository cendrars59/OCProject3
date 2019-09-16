# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*

import pygame
from appParams import parameters

# Application parameters initialization
#  - For screen sizing
#  - Game information
#  - Game is Running

screenWidth = parameters['screenSize']['width']
screenHeight = parameters['screenSize']['height']
gameName = parameters['gameInfo']['name']
gameVersion = parameters['gameInfo']['version']
isRunning = True

# Game initialization
# - Game init
# - Setting screen
# - Displaying game information
# - Set BackGround

pygame.init()
pygame.display.set_caption('{0}   Version: {1}'.format(gameName, gameVersion))
screen = pygame.display.set_mode((screenWidth, screenHeight))
background = pygame.image.load('purple-stone-background.jpg').convert()
screen.blit(background, (0, 0))
pygame.display.flip()

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()

exit()


