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
    def __getitem__(id):
        return AmberObject.get_item(id)

    @staticmethod
    def __delitem__(id):
        if id in database:
            del database[id]


import personal_docks
import seas
import ships


def is_personal_dock(in_object):
    return type(in_object) is personal_docks.PersonalDock


def is_sea(in_object):
    return type(in_object) is seas.Sea


def is_ship(in_object):
    return type(in_object) is ships.Ship


def export_database():
    file = open('database.db', 'w')
    file.write(str(AmberObject.current_available_id))
    file.write('++|++')
    for value in database.values():
        file.write(value.id)
        file.write('+|+')
        file.write(value.export_to_database())
        file.write('+|+')
        file.write(type(value))
        file.write('++|++')
    file.close()


def import_database():
    file = open('database.db', 'r')
    f_data = file.read().split('++|++')
    AmberObject.current_available_id = int(f_data[0])
    del f_data[0]
    for object in f_data:
        id, in_data, in_type = object.split('+|+')
        id = int(id)
        if in_type == "<class '__main__.PersonalDock'>":
            database[id] = personal_docks.PersonalDock.import_from_database(in_data)
        elif in_type == "<class '__main__.Sea'>":
            database[id] = seas.Sea.import_from_database(in_data)
        elif in_type == "<class '__main__.Ship'>":
            database[id] = ships.Ship.import_from_database(in_data)
    file.close()


import_database()
# start_gui_loop()
export_database()
