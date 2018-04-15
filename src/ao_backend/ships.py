"""
This file contains all ships related operations
"""

import amber
import datetime as dt


class ContentType(enumerate):
    Text = 0
    Image = 1
    Video = 2


class ShipPrivacy(enumerate):
    Only_creator = 0
    Only_friends = 1
    Only_followers = 2
    Only_friends_and_followers = 3
    Everyone = 3


class Ship(amber.AmberObject):

    """
    Ships class
    """

    @staticmethod
    def RegisterShip(creator_id, content_type, txt_content, image_content=None, video_content=None,
                     privacy=ShipPrivacy.Everyone, parent_ship=None):
        new = Ship(creator_id, content_type, txt_content, image_content, video_content, privacy, parent_ship)
        amber.database[new.id] = new

    def __init__(self, creator_id, content_type, txt_content, image_content=None, video_content=None,
                 privacy=ShipPrivacy.Everyone, parent_ship=None):
        super().__init__()
        self.creator_id = creator_id
        self.content_type = content_type
        self.txt_content = txt_content
        self.image_content = image_content
        self.video_content = video_content
        self.parent_ship = parent_ship
        self.creation_date = dt.datetime.utcnow().timetuple()
        self.privacy = privacy
        self.child_ships = []
        self.edit_history = [(txt_content, image_content, video_content, self.creation_date)]  # Tuples of four elements (text content, image content, video content, creation date)

    def export_to_file(self):
        pass

    def add_reply(self):
        pass

    def commit_edit(self):
        pass

    def change_privacy(self):
        pass

    @staticmethod
    def import_from_database(line):
        loaded_ship = Ship()
        return loaded_ship

    def export_to_database(self):
        line = str()
        return line
