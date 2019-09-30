# -*- coding: Utf-8 -*
from utils.files_management.import_items import build_list_from_file
from models.Item import Item


class Items_List:

    def __init__(self):
        self.list = build_list_from_file()

    def dispatch_items_randomly(self, level):
        """

        :param level:
        :return:
        """
        for item in self.list:
            item.position = Item.define_random_position(item, level)

    def find_an_item_in_list(self, level):
        for element in self.list:
            element.find_an_item(element, level)





