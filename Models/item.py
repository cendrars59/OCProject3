# -*- coding: Utf-8 -*
from random import randint


class Item:

    def __init__(self, name, icon_path):
        """
        Function to create an item
        :param name: Name of the item. Type string.
        :param icon_path: Path of the picture of the item. Type string.
        """
        self.name = name
        self.position = None
        self.icon_path = icon_path
        self.found = False

    def define_random_position(self, level):
        """
        defining a random position for an item.Position type is tuple
        :param level: level grid. Type labyrinth
        :return:
        """
        position_found = False
        able_to_find = False

        while not (position_found and able_to_find):
            row = randint(1, len(level.grid)-1)
            column = randint(1, len(level.grid[0])-1)
            if level.grid[row][column] != 'w':
                self.position = (row, column)
                level.grid[row][column] = 'i'
                position_found = True
                if self.be_able_to_find_it():
                    able_to_find = True
                else:
                    able_to_find = False

    def be_able_to_find_it(self):
        """
        Function to verify if the player can access to the item
        :return: A boolean
        """
        pass