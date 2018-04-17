"""
This file contains all seas related operations
"""

import amber
import datetime as dt


class SeaSailingPrivacy(enumerate):
    Only_administrators = 'onlyadministrators'
    Only_editors = 'onlyeditors'
    Everyone = 'everyone'


class SeaVisibilityPrivacy(enumerate):
    Only_Members = 'onlymembers'
    Everyone = 'everyone'


class Sea(amber.AmberObject):

    """
    Sea class
    """

    @staticmethod
    def RegisterSea(creator, name, description, visibility_privacy=SeaVisibilityPrivacy.Everyone,
                 sailing_privacy=SeaSailingPrivacy.Everyone):
        new = Sea(creator, name, description, visibility_privacy, sailing_privacy)
        amber.database[new.id] = new
        return new

    def __init__(self, creator, name, description, visibility_privacy=SeaVisibilityPrivacy.Everyone,
                 sailing_privacy=SeaSailingPrivacy.Everyone):
        super().__init__()
        self.creator = creator
        self.name = name
        self.description = description
        self.visibility_privacy = visibility_privacy
        self.sailing_privacy = sailing_privacy
        self.active = True
        self.administrators = [creator]
        self.editors = []
        self.members = [creator]
        self.sailed_ships = []  # Tuples of two elements (ship id, initial sailing date)
        self.creation_date = dt.datetime.utcnow().date()

    def deactivate(self):
        pass

    def change_name(self, name):
        pass

    def change_description(self, description):
        pass

    def is_administrator(self, id):
        pass

    def add_administrator(self, new_administrator_id):
        pass

    def remove_administrator(self, administrator_id):
        pass

    def is_editor(self, id):
        pass

    def add_editor(self, new_editor_id):
        pass

    def remove_editor(self, editor_id):
        pass

    def is_member(self, id):
        pass

    def add_member(self, new_member_id):
        pass

    def remove_member(self, member_id):
        pass

    def change_visibility_privacy(self, new_visibility_privacy):
        pass

    def change_sailing_privacy(self, new_sailing_privacy):
        pass

    def generate_ships(self):

        """
        Starts yielding posts shared to this sea chronologically
        """

        pass

    def sail_ship_to_this_sea(self, ship_id):
        pass

    def sink_ship_from_this_sea(self, ship_id):
        pass

    @staticmethod
    def import_from_database(line):
        loaded_sea = Sea()
        return loaded_sea

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
