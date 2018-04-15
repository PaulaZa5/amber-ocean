"""
This file contains all general operations
"""

database = {}


class AmberObject(object):

    """
    Base class for all objects on the network
    """

    current_available_id = 0

    @staticmethod
    def get_item(id):
        if id in database:
            return database[id]

    def __init__(self):
        self.id = AmberObject.current_available_id
        AmberObject.current_available_id += 1
        database[self.id] = self

    @staticmethod
    def __getitem__(item):
        return AmberObject.get_item(item)


import personal_docks
import seas
import ships


def is_personal_dock(in_object):
    return type(in_object) == personal_docks.PersonalDock


def is_sea(in_object):
    return type(in_object) == seas.Sea


def is_ship(in_object):
    return type(in_object) == ships.Ship


def export_database():
    file = open('database.db', 'w')
    for value in database.values():
        file.write(value.export_to_database())
        file.write('+|+')
        file.write(type(value))
        file.write('\n')
    file.close()


def import_database():
    file = open('database.db', 'r')
    for count, line in enumerate(file.readlines()):
        in_data, in_type = line.split('+|+')
        if in_type == "<class '__main__.PersonalDock'>":
            database[count] = personal_docks.PersonalDock.import_from_database(in_data)
        elif in_type == "<class '__main__.Sea'>":
            database[count] = seas.Sea.import_from_database(in_data)
        elif in_type == "<class '__main__.Ship'>":
            database[count] = ships.Ship.import_from_database(in_data)
    file.close()


import_database()
# start_gui_loop()
export_database()
