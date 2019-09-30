# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
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


# Function used for demo purpose
def print_grid():
    for row in level.grid:
        print(row)


not_stop = True
pygame.init()

while not_stop:
    pygame.display.set_caption('{0}   Version: {1}'.format(gameName, gameVersion))
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    background_picture_path = 'Resources//Pictures//purple-stone-background.jpg'
    background = pygame.image.load(background_picture_path).convert()
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            not_stop = False
            pygame.quit()

        elif event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                player.move(event.key, level)
                #player.gather_items(level, items_list)
                print(player.position)
                print_grid()
                for item in player.grabbedItems:
                    print(item.name)
                    print(item.found)

# Game initialization
# - Game init
# - Setting screen
# - Displaying game information
# - Set BackGround

# pygame.init()
#

# while isRunning:
#

# exit()
