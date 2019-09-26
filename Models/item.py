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

    def define_random_position(self, grid):
        """
        defining a random position for an item.Position type is tuple
        :param grid: level grid. Type labyrinth
        :return:
        """
        position_found = False

        while not position_found:
            row = randint(1, len(grid)-1)
            column = randint(1, len(grid[0])-1)
            if grid[row][column] != 'w':
                self.position = (row, column)
                grid[row][column] = 'i'
                position_found = True

