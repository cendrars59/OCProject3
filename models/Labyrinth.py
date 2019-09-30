# -*- coding: Utf-8 -*
from utils.files_management.import_maps import build_grid_from_file


class Labyrinth:
    """
    Class to manage the grid of the game according a provided map file.
    The grid is represented by 2 dimensional array.


    methods :
        - generating the grid according an input file.
        - defining the departure position
        - defining end position
        - defining the positions of the items to grab
        - getting the detailed items list.
    """

    def __init__(self, file):
        """
        initialization function in order to generate the game grid from a map file
        :param file: input txt file in order to generate the game grid
        """
        self.grid = build_grid_from_file(file)

    @property
    def departure(self):
        """
        Function to retrieve the departure position on the grid. Departure is define by the value d into the map
        file.
        :return: the departure position. Type is a tuple
        """
        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 's':
                    return index_row, index_column
                index_column += 1
            index_row += 1

    @property
    def end(self):
        """
        Function to retrieve the departure position on the grid. Departure is define by the value f into the map
        file.
        :return: the departure position. Type is a tuple
        """
        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 'e':
                    return index_row, index_column
                index_column += 1
            index_row += 1

    # To review
    def dispatch_items_randomly(self, items_list):

        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 'i':
                    position = (index_row, index_column)
                    items_list.append(position)

                index_column += 1
            index_row += 1
        return items_list

    def get_items_list(self, params):

        items_list = dict(params)
        position_list = self.get_items_position(items_list)

        count = 0
        for key, value in items_list.items():
            position_attribute = {'position': position_list[count]}
            value.update(position_attribute)
            count += 1
        return items_list

    def find_next_value_on_grid(self, player_next_row, player_next_column):
        """
        function to calculate the next value on the grid according the move of the player
        :param player_next_row: calculated next row number according the player's move .Type int.
        :param player_next_column: calculated next row number according the player's move .Type int.
        :return: value of Type string
        """

        if self.grid[player_next_row][player_next_column] == '0':
            return 'p'
        elif self.grid[player_next_row][player_next_column] == 'i':
            return 'i'
        elif self.grid[player_next_row][player_next_column] == 'f':
            return 'f'
        elif self.grid[player_next_row][player_next_column] == 'e':
            return 'e'
        elif self.grid[player_next_row][player_next_column] == 'p':
            return 'p'






