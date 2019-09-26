# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*

import pygame
from parameters.app_params import parameters
from parameters.items_params import items
import models.Persona
import models.Labyrinth
import models.Item

# Labyrinth initialization
path_to_map_file = 'Resources//Maps//map1.txt'
level = models.Labyrinth.Labyrinth(path_to_map_file)


# List of items building up and placing on grid
items_list = []
for key, value in items.items():
    item = models.Item.Item(value['name'], value['icon'])
    item.define_random_position(level.grid)
    items_list.append(item)


# Windows initialization

screenWidth = parameters['screenSize']['width']
screenHeight = parameters['screenSize']['height']
gameName = parameters['gameInfo']['name']
gameVersion = parameters['gameInfo']['version']
isRunning = True

# Persona initialization
player = models.Persona.Persona(level.departure, 'Mac Gyver', 'Alive', True, 'Resources//Pictures//MacGyver.png',
                                items_list)
enemy = models.Persona.Persona(level.departure, 'The bad guy', 'Bad guy', False, 'Resources//Pictures//Gardien.png',
                               None)

# Game initialization
# - Game init
# - Setting screen
# - Displaying game information
# - Set BackGround

# pygame.init()
# pygame.display.set_caption('{0}   Version: {1}'.format(gameName, gameVersion))
# screen = pygame.display.set_mode((screenWidth, screenHeight))
# background_picture_path = 'Resources//Pictures//purple-stone-background.jpg'
# background = pygame.image.load(background_picture_path).convert()
# screen.blit(background, (0, 0))
# pygame.display.flip()

# while isRunning:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#           isRunning = False
#           pygame.quit()

# exit()
