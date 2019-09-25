# -*- coding: Utf-8 -*
from Tools.FilesManagement.import_maps import build_grid_from_file


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


    def get_departure(self):
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
                    return index_row + 1, index_column + 1
                index_column += 1
            index_row += 1

    def get_end(self):
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
                    return index_row + 1, index_column + 1
                index_column += 1
            index_row += 1

    # To review
    def get_item_position(self, items_list):

        items_list = []
        index_row = 0
        for row in self.grid:
            index_column = 0
            for c in row:
                if c == 'i':
                    position = (index_row + 1, index_column + 1)
                    items_list.append(position)

                index_column += 1
            index_row += 1
        return items_list

    def get_items_list(self, params):

        items_list = dict(params)
        position_list = self.get_items_position()

        count = 0
        for key, value in items_list.items():
            position_attribute = {'position': position_list[count]}
            value.update(position_attribute)
            count += 1
        return items_list



