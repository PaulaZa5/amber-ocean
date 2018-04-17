"""
This file contains all ships related operations
"""

import amber
import datetime as dt


class ContentType(enumerate):
    Text = 'text'
    Image = 'image'
    Video = 'video'


class Reactions(enumerate):
    Like = 'like'
    Dislike = 'dislike'
    Love = 'love'
    Angry = 'angry'
    Haha = 'haha'


class ShipPrivacy(enumerate):
    Only_creator = 'onlycreator'
    Only_friends = 'onlyfriends'
    Only_followers = 'onlyfollowers'
    Only_friends_and_followers = 'onlyfriendsandfollowers'
    Everyone = 'everyone'


class Ship(amber.AmberObject):

    """
    Ships class
    """

    @staticmethod
    def RegisterShip(creator_id, where_is_it_created_id, content_type, txt_content, image_content=None, video_content=None,
                     privacy=ShipPrivacy.Everyone, parent_ship_id=None):
        new = Ship(creator_id, where_is_it_created_id, content_type, txt_content, image_content, video_content, privacy, parent_ship_id)
        amber.database[new.id] = new
        return new

    def __init__(self, creator_id, where_is_it_created_id, content_type, txt_content, image_content=None, video_content=None,
                 privacy=ShipPrivacy.Everyone, parent_ship_id=None):
        super().__init__()
        self.creator_id = creator_id
        self.where_is_it_created_id = where_is_it_created_id
        self.content_type = content_type
        self.txt_content = txt_content
        self.image_content = image_content
        self.video_content = video_content
        self.privacy = privacy
        self.reactions = {Reactions.Like: [], Reactions.Dislike: [], Reactions.Love: [], Reactions.Angry: [],
                          Reactions.Haha: []}  # Add ids of personal docks in the list
        self.parent_ship_id = parent_ship_id
        self.creation_date = dt.datetime.utcnow().timetuple()
        self.child_ships = []
        self.edit_history = []  # Tuples of four elements (text content, image content, video content, creation date)

    def add_reply(self, replayer_id, replay_type, replay_text, replay_image=None, replay_video=None):
        pass

    def add_reaction(self, reactioner_id, reaction):
        pass

    def change_reaction(self, reactioner_id, new_reaction):
        pass

    def remove_reaction(self, reactioner_id):
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
