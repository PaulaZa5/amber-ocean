"""
This file contains all ships related operations
"""

import amber
import datetime as dt


class ContentType(enumerate):
    Text = 0
    Image = 1
    Video = 2


class Reactions(enumerate):
    Like = 0
    Dislike = 1
    Love = 2
    Angry = 3
    Haha = 4


class ShipPrivacy(enumerate):
    Only_creator = 0
    Only_friends = 1
    Only_followers = 2
    Only_friends_and_followers = 3
    Everyone = 4


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
        self.privacy = privacy
        self.reactions = {Reactions.Like: [], Reactions.Dislike: [], Reactions.Love: [], Reactions.Angry: [],
                          Reactions.Haha: []}  # Add ids of personal docks in the list
        self.parent_ship = parent_ship
        self.creation_date = dt.datetime.utcnow().timetuple()
        self.child_ships = []
        self.edit_history = [(txt_content, image_content, video_content, self.creation_date)]  # Tuples of four elements (text content, image content, video content, creation date)

    def add_reply(self, replayer_id, replay_text):
        pass

    def add_reaction(self, reactioner_id, reaction):
        pass

    def commit_edit(self, edit_text, edit_image=None, edit_video=None):
        pass

    def change_privacy(self, new_privacy):
        pass

    @staticmethod
    def import_from_database(line):
        loaded_ship = Ship()
        return loaded_ship

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
