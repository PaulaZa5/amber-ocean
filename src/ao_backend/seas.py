"""
This file contains all seas related operations
"""

import amber
import datetime as dt


class SeaSailingPrivacy(enumerate):
    Only_administrators = 0
    Only_editors = 1
    Everyone = 2


class SeaVisibilityPrivacy(enumerate):
    Only_Members = 0
    Everyone = 1


class Sea(amber.AmberObject):

    """
    Sea class
    """

    @staticmethod
    def RegisterSea(creator, name, description):
        new = Sea(creator, name, description)
        amber.database[new.id] = new

    def __init__(self, creator, name, description):
        super().__init__()
        self.creator = creator
        self.name = name
        self.description = description
        self.administrators = [creator]
        self.editors = []
        self.members = [creator]
        self.visibility_privacy = SeaVisibilityPrivacy.Everyone
        self.sailing_privacy = SeaSailingPrivacy.Everyone
        self.creation_date = dt.datetime.utcnow().date()
        self.sailed_ships = []  # Tuples of two elements (ship id, initial sailing date)

    def export_to_file(self):
        pass

    def add_administrator(self):
        pass

    def remove_administrator(self):
        pass

    def add_editor(self):
        pass

    def remove_editor(self):
        pass

    def add_member(self):
        pass

    def remove_member(self):
        pass

    def change_visibility_privacy(self):
        pass

    def change_sailing_privacy(self):
        pass

    def add_to_sailed_ships(self):
        pass

    @staticmethod
    def import_from_database(line):
        loaded_sea = Sea()
        return loaded_sea

    def export_to_database(self):
        line = str()
        return line
