# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from parameters.app_params import parameters
import models.Persona
import models.Labyrinth
import models.Items_List

# Labyrinth initialization
path_to_map_file = 'resources//Maps//map1.txt'
level = models.Labyrinth.Labyrinth(path_to_map_file)


# List of items building up and placing on grid

items = models.Items_List.Items_List()
items.dispatch_items_randomly(level)



# Windows initialization

screenWidth = parameters['screenSize']['width']
screenHeight = parameters['screenSize']['height']
gameName = parameters['gameInfo']['name']
gameVersion = parameters['gameInfo']['version']
isRunning = True

# Persona initialization
player = models.Persona.Persona(level.departure, 'Mac Gyver', 'Alive', True, 'Resources//Pictures//MacGyver.png',                                items.list)
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
                player.find_item(level)
                for item in player.grabbedItems:
                    print(item.name)
                    print(item.found)
                    print(item.position)
                print_grid()


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
