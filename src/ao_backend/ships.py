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
    def RegisterShip(creator_id, where_is_it_created_id, content_type, txt_content, image_content=None,
                     video_content=None, privacy=ShipPrivacy.Everyone, parent_ship_id=None, new_object=True):
        new = Ship(creator_id, where_is_it_created_id, content_type, txt_content, image_content, video_content,
                   privacy, parent_ship_id, new_object)
        amber.database[new.id] = new
        return new

    def __init__(self, creator_id, where_is_it_created_id, content_type, txt_content, image_content=None, video_content=None,
                 privacy=ShipPrivacy.Everyone, parent_ship_id=None, new_object=True):
        super().__init__(new_object)
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
        Ship.RegisterShip(replayer_id, self.where_is_it_created_id, replay_type, replay_text,
                                   replay_image, replay_video, ShipPrivacy.Everyone, self.id)
        return True

    def add_reaction(self, reactioner_id, reaction):
        if reaction in self.reactions.keys():
            self.reactions[reaction].append(reactioner_id)
            return True
        return False

    def change_reaction(self, reactioner_id, new_reaction):
        return self.remove_reaction(reactioner_id) & self.add_reaction(reactioner_id, new_reaction)

    def remove_reaction(self, reactioner_id):
        for lst in self.reactions.values():
            for id in lst:
                if id == reactioner_id:
                    lst.remove(id)
                    return True
        return False

    def commit_edit(self, edit_text, edit_image=None, edit_video=None):
        self.edit_history.append((self.txt_content, self.image_content, self.video_content, self.creation_date))
        self.txt_content = edit_text
        self.image_content = edit_image
        self.video_content = edit_video
        self.creation_date = dt.datetime.utcnow().timetuple()
        return True

    def change_privacy(self, new_privacy):
        self.privacy = new_privacy
        return True

    def comments_no(self):
        return len(self.child_ships)

    def __len__(self):
        return len(self.child_ships)

    def generate_comments(self):

        """
        Starts yielding comments on this ship
        """

        for ship in self.child_ships:
            yield ship

    @staticmethod
    def import_from_database(line):
        loaded_ship = Ship()
        return loaded_ship

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
