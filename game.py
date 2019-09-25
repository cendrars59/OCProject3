# !C:\Users\cyrle\AppData\Local\Programs\Python\Python37
# -*- coding: Utf-8 -*

import pygame
from Parameters.appParams import parameters
from Parameters.itemsParams import items
import Models.persona
import Models.labyrinth
import Models.item

# Labyrinth initialization
path_to_map_file = 'Resources//Maps//map1.txt'
level = Models.labyrinth.Labyrinth(path_to_map_file)
start_position = level.get_departure()
end_position = level.get_end()

# List of items building up and placing on grid
items_list = []
for key, value in items.items():
    item = Models.item.Item(value['name'], value['icon'])
    item.define_random_position(level.grid)
    items_list.append(item)


# Windows initialization

screenWidth = parameters['screenSize']['width']
screenHeight = parameters['screenSize']['height']
gameName = parameters['gameInfo']['name']
gameVersion = parameters['gameInfo']['version']
isRunning = True

# Persona initialization
player = Models.persona.Persona(start_position, 'Mac Gyver', 'Alive', True, 'Resources//Pictures//MacGyver.png',
                                items_list)
enemy = Models.persona.Persona(end_position, 'The bad guy', 'Bad guy', False, 'Resources//Pictures//Gardien.png',
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
