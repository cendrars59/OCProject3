# -*- coding: Utf-8 -*
from pygame.constants import K_DOWN
from pygame.constants import K_UP
from pygame.constants import K_LEFT
from pygame.constants import K_RIGHT


class Persona:
    """
    class  in order to create instance of game persona
    caracteristics :
        - position : position on the grid defined by a tuple (row, column)
        - name : name of persona. Type string
        - isGood : define if the persona is a good guy. Type boolean
        - isMoving : define if the persona is allowed to move. Type boolean
        - icon : path to the picture of the persona. Type string
        - grabbedItems : list of items collected by persona. Type list

    methods :
        - persona can move up, down, back, forward.
        - persona gathers items
        - persona can win or lose
    """

    def __init__(self, position, name, status, is_moving, icon, items_list):
        """

        :param position: current position of the persona. Type is tuple
        :param name: name of the persona. Type is string
        :param status: Status can the following value 'alive', bad guy', 'dead', 'winner'. Type is string
        :param is_moving: persona is allowed to move. Type is boolean
        :param icon: path to the picture to get the persona icon. Type is string
        :param items_list: list of items to retrieve. Type is dictionary
        """

        self.position = position
        self.name = name
        self.status = status
        self.is_moving = is_moving
        self.icon = icon
        self.grabbedItems = items_list

    def find_item(self, level):
        """
        function to identify the items found by player along the game.
        :param level: game grid represented by a 2 dimensional array.
        :return:
        """

        if level.grid[self.position[0]][self.position[1]] == 'i':
            for item in self.grabbedItems:
                if item.position == self.position:
                    item.found = True
                    item.icon_path = "{0}_found.png".format(item.name)
                    level.grid[self.position[0]][self.position[1]] = 'f'
        
    @property
    def has_sering(self):
        """
        Function to verify if all items belonging to the list have been found.
        :return:
        """

        found_count = 0
        for item in self.grabbedItems:
            if item.found:
                found_count += 1

        if found_count == len(self.grabbedItems):
            return True

    def end_game(self, end_position):
        """

        :param end_position:
        :return:
        """
        if self.position == end_position and self.has_sering:
            self.status = 'winner'
        elif self.position == end_position and not self.has_sering:
            self.status = 'dead'
        else:
            self.status = 'alive'

    def move(self, key, level):
        """
        Function to manage the moves of the player according the stroke key.
        User is not allowed to get off the grid or on a wall position. In such case, player stays at the same
        position.

        :param level: game level. Type labyrinth.
        :param key: stroke key. Type string.
        :return:
        """
        print(key)
        next_value_on_grid = None
        # move forward
        if key == K_RIGHT and self.position[1] + 1 <= len(level.grid[0]) and\
                level.grid[self.position[0]][self.position[1] + 1] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0], self.position[1] + 1)
            self.position = self.position[0], self.position[1] + 1
            level.grid[self.position[0]][self.position[1]-1] = '0'  # removing the older player position

        # move back
        elif key == K_LEFT and self.position[1] - 1 >= 0 and level.grid[self.position[0]][self.position[1] - 1] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0], self.position[1] - 1)
            self.position = self.position[0], self.position[1] - 1
            level.grid[self.position[0]][self.position[1]+1] = '0'  # removing the older player position

        # move up
        elif key == K_UP and self.position[0] - 1 >= 0 and level.grid[self.position[0] - 1][self.position[1]] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0] - 1, self.position[1])
            self.position = self.position[0] - 1, self.position[1]
            level.grid[self.position[0]+1][self.position[1]] = '0'  # removing the older player position

        # move down
        elif key == K_DOWN and self.position[0] + 1 <= len(level.grid) and\
                level.grid[self.position[0]+1][self.position[1]] != 'w':
            next_value_on_grid = level.find_next_value_on_grid(self.position[0] + 1, self.position[1])
            self.position = self.position[0] + 1, self.position[1]
            level.grid[self.position[0] - 1][self.position[1]] = '0'  # removing the older player position

        # no move
        else:
            self.position = self.position

        level.grid[self.position[0]][self.position[1]] = next_value_on_grid  # Set new value according new position

