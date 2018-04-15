"""
This file contains all personal-docks related operations
"""

import amber
import datetime as dt
import hashlib


class RelationshipStates(enumerate):
    Single = 0
    In_a_relationship = 1
    Engaged = 2
    Married = 3
    Separated = 4
    In_an_open_relationship = 5
    Complicated = 6
    Divorced = 7
    Widowed = 8


class FamilyRelationship(enumerate):
    Brother = 0
    Sister = 1
    Father = 2
    Mother = 3
    Son = 4
    Daughter = 5
    Uncle = 6
    Aunt = 7
    Nephew = 8
    Niece = 9
    Cousin = 10
    Grandmother = 11
    Granddaughter = 12
    Stepbrother = 13
    Stepsister = 14
    Stepfather = 15
    Stepmother = 16
    Stepson = 17
    Stepdaughter = 18
    Brother_in_law = 19
    Sister_in_law = 20
    Father_in_law = 21
    Mother_in_law = 22
    Son_in_law = 23
    Daughter_in_law = 24


class PersonalDock(amber.AmberObject):

    """
    Personal Dock class
    """

    @staticmethod
    def RegisterAccount(name, gender, birthday, email, password):
        new = PersonalDock(name, gender, birthday, email, password)
        amber.database[new.id] = new

    def __init__(self, name, gender, birthday, email, password):
        super().__init__()
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.master_email = email
        self.emails = [email]
        self.password = hashlib.sha224(password).hexdigest()  # Encrypted password
        self.join_date = dt.datetime.utcnow().date()
        self.friends = []
        self.following = []
        self.followers = []
        self.seas = []
        self.family = []  # Tuples of two elements (person id, family relationship type)
        self.education = []  # Tuples of four elements (major, place of education, starting date, finishing date)
        self.living_in = []  # Tuples of three elements (location, starting date, finishing date)
        self.relationship_status = RelationshipStates.Single
        self.relationships = []  # Tuples of four elements (significant other id, type, starting date, finishing date)
        self.links = []  # Tuples of two elements (link string=>(facebook, linkedin..etc), link url)
        self.special_fields = []  # Tuples of two elements (field string=>(nickname, about..etc), field text)
        self.sailed_ships = []  # Tuples of two elements (ship id, initial sailing date)

    def export_to_file(self):
        pass

    def change_name(self):
        pass

    def change_gender(self):
        pass

    def change_birthday(self):
        pass

    def change_master_email(self):
        pass

    def change_password(self):
        pass

    def add_email(self):
        pass

    def add_friend(self):
        pass

    def remove_friend(self):
        pass

    def add_follower(self):
        pass

    def remove_follower(self):
        pass

    def add_following(self):
        pass

    def remove_following(self):
        pass

    def add_family_member(self):
        pass

    def add_education(self):
        pass

    def add_living_place(self):
        pass

    def add_relationship(self):
        pass

    def add_link(self):
        pass

    def sail_ship(self, where_to_id):  # where_to_id is some post's id, dock's id or sea's id
        pass

    @staticmethod
    def import_from_database(line):
        loaded_personal_dock = PersonalDock()
        return loaded_personal_dock

    def export_to_database(self):
        line = str()
        return line
