"""
This file contains all personal-docks related operations
"""

import amber
import datetime as dt
import hashlib


class FamilyRelationship(enumerate):
    Brother = 'brother'
    Sister = 'sister'
    Father = 'father'
    Mother = 'mother'
    Son = 'son'
    Daughter = 'daughter'
    Uncle = 'uncle'
    Aunt = 'aunt'
    Nephew = 'nephew'
    Niece = 'niece'
    Cousin = 'cousin'
    Grandmother = 'grandmother'
    Granddaughter = 'granddaughter'
    Stepbrother = 'stepbrother'
    Stepsister = 'stepsister'
    Stepfather = 'stepfather'
    Stepmother = 'stepmother'
    Stepson = 'stepson'
    Stepdaughter = 'stepdaughter'
    Brother_in_law = 'brotherinlaw'
    Sister_in_law = 'sisterinlaw'
    Father_in_law = 'fatherinlaw'
    Mother_in_law = 'motherinlaw'
    Son_in_law = 'soninlaw'
    Daughter_in_law = 'daughterinlaw'


class Gender(enumerate):
    Male = 'male'
    Female = 'female'
    Other = 'other'


class RelationshipStates(enumerate):
    Single = 'single'
    In_a_relationship = 'inarelationship'
    Engaged = 'engaged'
    Married = 'marriend'
    Separated = 'separated'
    In_an_open_relationship = 'inanopenrelationship'
    Complicated = 'complicated'
    Divorced = 'divorced'
    Widowed = 'widowed'


class PersonalDock(amber.AmberObject):

    """
    Personal Dock class
    """

    @staticmethod
    def RegisterAccount(name, gender, birthday, password, email=None, phone_number=None):
        new = PersonalDock(name, gender, birthday, password, email, phone_number)
        amber.database[new.id] = new
        return new

    def __init__(self, name, gender, birthday, password, email=None, phone_number=None):
        super().__init__()
        self.name = name
        self.gender = gender
        self.birthday = birthday  # dt.datetime.date()
        self.password = hashlib.sha224(password).hexdigest()  # Encrypted password
        self.master_email = email
        self.emails = [email]
        self.master_phone_number = phone_number
        self.phone_numbers = [phone_number]
        self.active = True
        self.friends = []
        self.followers = []
        self.followees = []
        self.seas = []
        self.family = []  # Tuples of two elements (person id, family relationship type)
        self.education = []  # Tuples of four elements (major, place of education, starting date, finishing date)
        self.living_in = []  # Tuples of three elements (location, starting date, finishing date)
        self.relationship_status = RelationshipStates.Single
        self.relationships = []  # Tuples of four elements (significant other id, type, starting date, finishing date)
        self.links = []  # Tuples of two elements (link string=>(facebook, linkedin..etc), link url)
        self.special_fields = []  # Tuples of two elements (field string=>(nickname, about..etc), field text)
        self.sailed_ships = []  # Tuples of two elements (ship id, initial sailing date)
        self.join_date = dt.datetime.utcnow().date()

    def deactivate_account(self):
        pass

    def change_name(self, password, new_name):
        pass

    def change_gender(self, password, new_gender):
        pass

    def change_birthday(self, password, new_birthday):
        pass

    def change_password(self, password, new_password):
        pass

    def change_master_email(self, password, new_email):
        pass

    def add_email(self, new_email):
        pass

    def remove_email(self, email):
        pass

    def change_master_phone_number(self, password, new_phone_number):
        pass

    def add_phone_number(self, new_phone_number):
        pass

    def remove_phone_number(self, phone_number):
        pass

    def add_friend(self, friend_id):
        pass

    def remove_friend(self, friend_id):
        pass

    def add_follower(self, follower_id):
        pass

    def remove_follower(self, follower_id):
        pass

    def add_followee(self, followee_id):
        pass

    def remove_followee(self, followee_id):
        pass

    def add_family_member_relationship(self, family_member_id, family_member_relation):
        pass

    def edit_family_member_relationship(self, family_member_id, new_family_member_relation):
        pass

    def remove_family_member_relationship(self, family_member_id):
        pass

    def add_education(self, major, place_of_education, starting_date, finishing_date):
        pass

    def edit_education(self, major, place_of_education, new_starting_date, new_finishing_date):
        pass

    def remove_education(self, major, place_of_education):
        pass

    def add_living_place(self, location, starting_date, finishing_date):
        pass

    def edit_living_place(self, location, new_starting_date, new_finishing_date):
        pass

    def remove_living_place(self, location):
        pass

    def add_relationship(self, significant_other_id, type, starting_date, finishing_date):
        pass

    def edit_relationship(self, significant_other_id, new_type, new_starting_date, new_finishing_date):
        pass

    def remove_relationship(self, significant_other_id):
        pass

    def add_link(self, link_string, link_url):
        pass

    def edit_link_url(self, link_string, new_link_url):
        pass

    def remove_link(self, link_string):
        pass

    def add_special_field(self, special_field_string, special_field_text):
        pass

    def edit_special_field_text(self, special_field_string, new_special_field_text):
        pass

    def remove_special_field(self, special_field_string):
        pass

    def sail_ship_to_this_dock(self, ship_id):
        pass

    def sink_ship_from_this_dock(self, ship_id):
        pass

    @staticmethod
    def import_from_database(line):
        loaded_personal_dock = PersonalDock()
        return loaded_personal_dock

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
