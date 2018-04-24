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

    def __init__(self, new_object):
        if new_object:
            self.id = AmberObject.current_available_id
            AmberObject.current_available_id += 1
            database[self.id] = self
        else:
            self.id = None

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

def generate_personal_docks():
    for memberid,member in database.items():
        if is_personal_dock(member):
            yield member

def most_friends_members_generator(limit):
    maxfriends=0
    minfriends=0
    maxfriends_id=-1
    members=generate_personal_docks()
    for i in range(limit):
        for member in members:
            if (len(member.friends)>maxfriends and len(member.friends)<=minfriends and maxfriends_id is not member.id) or (len(member.friends)>maxfriends and i==0):
                maxfriends=len(member.friends)
                maxfriends_id=member.id
        yield maxfriends_id,maxfriends
        minfriends=maxfriends
        maxfriends=0

def most_followers_members_generator(limit):
    maxfollowers=0
    minfollowers=0
    maxfollowers_id=-1
    members = generate_personal_docks()
    for i in range(limit):
        for member in members:
            if (len(member.followers)>maxfollowers and len(member.followers)<=minfollowers and maxfollowers_id is not member.id) or (len(member.followers)>maxfollowers and i==0):
                maxfollowers=len(member.followers)
                maxfollowers_id=member.id
        yield maxfollowers_id,maxfollowers
        minfollowers=maxfollowers
        maxfollowers=0

def max_reactions_ship_for_each_member_generator():
    for member in generate_personal_docks():
       yield member.max_reactions_ship()

def max_comments_ship_for_each_member_generator():
    for member in generate_personal_docks():
       yield member.max_comments_ship()


def is_sea(in_object):
    return type(in_object) is seas.Sea

def generate_seas():
    for memberid,member in database.items():
        if is_sea(member):
            yield member

def most_members_seas_generator(limit):
    maxmembers=0
    minmembers=0
    maxmembers_id=-1
    groups=generate_seas()
    for i in range(limit):
        for group in groups:
            if (len(group.members)>maxmembers and len(group.members)<=minmembers and maxmembers_id is not group.id) or (len(group.members)>maxmembers and i==0):
                maxmembers=len(group.members)
                maxmembers_id=group.id
        yield maxmembers_id,maxmembers
        minmembers=maxmembers
        maxmembers=0

def most_posts_seas_generator(limit):
    maxposts=0
    minposts=0
    maxposts_id=-1
    groups=generate_seas()
    for i in range(limit):
        for group in groups:
            if (len(group.sailed_ships)>maxposts and len(group.sailed_ships)<=minposts and maxposts_id is not group.id) or (len(group.sailed_ships)>maxposts and i==0):
                maxposts=len(group.sailed_ships)
                maxposts_id=group.id
        yield maxposts_id,maxposts
        minposts=maxposts
        maxposts=0


def max_reactions_ship_for_each_sea_generator():
    for member in generate_seas():
       yield member.max_reactions_ship()

def max_comments_ship_for_each_sea_generator():
    for member in generate_seas():
       yield member.max_comments_ship()

def is_ship(in_object):
    return type(in_object) is ships.Ship

def generate_ships():
    for memberid,member in database.items():
        if is_ship(member):
            yield member


def export_database():
    file = open('database.db', 'w')
    file.write(str(AmberObject.current_available_id))
    file.write('++|++')
    for value in database.values():
        file.write(str(value.id))
        file.write('+|+')
        file.write(value.export_to_database())
        file.write('+|+')
        file.write(str(type(value)))
        file.write('++|++')
    file.close()


def import_database():
    file = open('database.db', 'r')
    f_data = file.read().split('++|++')
    AmberObject.current_available_id = int(f_data[0])
    del f_data[0]
    del f_data[len(f_data) - 1]
    for object in f_data:
        id, in_data, in_type = object.split('+|+')
        id = int(id)
        if in_type == "<class 'personal_docks.PersonalDock'>":
            database[id] = personal_docks.PersonalDock.import_from_database(in_data)
            database[id].id = id
        elif in_type == "<class 'seas.Sea'>":
            database[id] = seas.Sea.import_from_database(in_data)
            database[id].id = id
        elif in_type == "<class 'ships.Ship'>":
            database[id] = ships.Ship.import_from_database(in_data)
            database[id].id = id
    file.close()


import_database()
# start_gui_loop()
export_database()
