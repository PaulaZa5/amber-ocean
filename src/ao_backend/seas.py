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
        self.active = False
        return True

    def change_name(self, name):
        self.name = name
        return True

    def change_description(self, description):
        self.description = description
        return True

    def is_administrator(self, id):
        return id in self.administrators

    def add_administrator(self, new_administrator_id):
        self.administrators.append(new_administrator_id)
        return True

    def remove_administrator(self, administrator_id):
        self.administrators.remove(administrator_id)
        return True

    def is_editor(self, id):
        return id in self.editors


    def add_editor(self, new_editor_id):
        self.editors.append(new_editor_id)
        return True

    def remove_editor(self, editor_id):
        self.editors.remove(editor_id)
        return True

    def is_member(self, id):
        return id in self.members

    def add_member(self, new_member_id):
        self.members.append(new_member_id)
        return True

    def remove_member(self, member_id):
        self.members.remove(member_id)
        return True

    def change_visibility_privacy(self, new_visibility_privacy):
        self.visibility_privacy = new_visibility_privacy
        return True

    def change_sailing_privacy(self, new_sailing_privacy):
        self.sailing_privacy = new_sailing_privacy
        return True


    def generate_ships(self):
        """
        Starts yielding posts shared to this sea chronologically
        """
        pass

    def sail_ship_to_this_sea(self, ship_id):
        self.sailed_ships.append((ship_id , dt.datetime.utcnow().date()))
        return True

    def sink_ship_from_this_sea(self, ship_id):
        for ship,date in self.sailed_ships:
            if ship == ship_id:
                self.sailed_ships.remove(ship)
        return True

    @staticmethod
    def import_from_database(line):
        loaded_sea = Sea()
        return loaded_sea

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
