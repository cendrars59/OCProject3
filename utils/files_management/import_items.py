import models.Item
from parameters import items_params


def build_list_from_file():
    items_list = []
    for key, value in items_params.items.items():
        temp_item = models.Item.Item(value['name'], value['icon'])
        items_list.append(temp_item)
    return items_list

