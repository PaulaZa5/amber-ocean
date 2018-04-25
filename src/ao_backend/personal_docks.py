"""
This file contains all personal-docks related operations
"""
import amber
from amber import database
import datetime as dt
import hashlib
import sortedcontainers
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
    Married = 'married'
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
    def RegisterAccount(name, gender, birthday, password, email=None, phone_number=None, new_object=True):
        new = PersonalDock(name, gender, birthday, password, email, phone_number, new_object)
        amber.database[new.id] = new
        return new

    def __init__(self, name, gender, birthday, password, email=None, phone_number=None, new_object=True):
        super().__init__(new_object)
        self.name = name
        self.gender = gender
        self.birthday = birthday  # dt.datetime.date()
        self.password = hashlib.sha224(password.encode('utf-8')).hexdigest()  # Encrypted password
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

    def check_password(self, password):
        password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        return self.password is password

    def deactivate_account(self):
        self.active = False
        return True

    def change_name(self, new_name):
        self.name = new_name
        return True

    def change_gender(self, new_gender):
        self.gender = new_gender
        return True

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
        return True

    def change_password(self, new_password):
        self.password = hashlib.sha224(new_password.encode('utf-8')).hexdigest()
        return True

    def change_master_email(self, new_email):
        self.master_email = new_email
        return True

    def add_email(self, new_email):
        self.emails.append(new_email)
        return True

    def remove_email(self, email):
        self.emails.remove(email)
        return True

    def change_master_phone_number(self, new_phone_number):
        self.master_phone_number = new_phone_number
        return True

    def add_phone_number(self, new_phone_number):
        self.phone_numbers.append(new_phone_number)
        return True

    def remove_phone_number(self, phone_number):
        self.phone_numbers.remove(phone_number)
        return True

    def add_friend(self, friend_id):
        self.friends.append(friend_id)
        return True

    def remove_friend(self, friend_id):
        self.friends.remove(friend_id)
        return True

    def add_follower(self, follower_id):
        self.followers.append(follower_id)
        return True

    def remove_follower(self, follower_id):
        self.followers.remove(follower_id)
        return True

    def add_followee(self, followee_id):
        self.followees.append(followee_id)
        return True

    def remove_followee(self, followee_id):
        self.followees.remove(followee_id)
        return True

    def add_family_member_relationship(self, family_member_id, family_member_relation):
        self.family.append((family_member_id, family_member_relation))
        return True

    def edit_family_member_relationship(self, family_member_id, new_family_member_relation):
        for fam_member, fam_relation in self.family:
            if fam_member is family_member_id:
                fam_relation = new_family_member_relation
                return True
        return False

    def remove_family_member_relationship(self, family_member_id):
        for fam_member, fam_relation in self.family:
            if fam_member is family_member_id:
                self.family.remove((family_member_id, fam_relation))
                return True
        return False

    def add_education(self, major, place_of_education, starting_date, finishing_date):
        self.education.append((major, place_of_education, starting_date, finishing_date))
        return True

    def edit_education(self, major, place_of_education, new_starting_date, new_finishing_date):
        for maj, place, start, finish in self.education:
            if maj is major and place is place_of_education:
                start = new_starting_date
                finish = new_finishing_date
                return True
        return False

    def remove_education(self, major, place_of_education):
        for maj, place, start, finish in self.education:
            if maj is major and place is place_of_education:
                self.education.remove((maj, place, start, finish))
                return True
        return False

    def add_living_place(self, location, starting_date, finishing_date):
        self.living_in.append((location, starting_date, finishing_date))
        return True

    def edit_living_place(self, location, new_starting_date, new_finishing_date):
        for loc, start, finish in self.living_in:
            if loc is location:
                start = new_starting_date
                finish = new_finishing_date
                return True
        return False

    def remove_living_place(self, location):
        for loc, start, finish in self.living_in:
            if loc is location:
                self.living_in.remove((loc, start, finish))
                return True
        return False

    def add_relationship(self, significant_other_id, type, starting_date, finishing_date):
        self.relationships.append((significant_other_id, type, starting_date, finishing_date))
        return True

    def edit_relationship(self, significant_other_id, new_type, new_starting_date, new_finishing_date):
        for sign_id, rel_type, start, finish in self.relationships:
            if sign_id is significant_other_id:
                rel_type = new_type
                start = new_starting_date
                finish = new_finishing_date
                return True
        return False

    def remove_relationship(self, significant_other_id):
        for sign_id, rel_type, start, finish in self.relationships:
            if sign_id is significant_other_id:
                self.relationships.remove((sign_id, rel_type, start, finish))
                return True
        return False

    def add_link(self, link_string, link_url):
        self.links.append((link_string, link_url))
        return True

    def edit_link_url(self, link_string, new_link_url):
        for link_str, link_url in self.links:
            if link_str is link_string:
                link_url = new_link_url
                return True
        return False

    def remove_link(self, link_string):
        for link_str, link_url in self.links:
            if link_str is link_string:
                self.links.remove((link_str, link_url))
                return True
        return False

    def add_special_field(self, special_field_string, special_field_text):
        self.special_fields.append((special_field_string, special_field_text))
        return True

    def edit_special_field_text(self, special_field_string, new_special_field_text):
        for field_str, field_txt in self.special_fields:
            if field_str is special_field_string:
                field_txt = new_special_field_text
                return True
        return False

    def remove_special_field(self, special_field_string):
        for field_str, field_txt in self.special_fields:
            if field_str is special_field_string:
                self.special_fields.remove((field_str, field_txt))
                return True
        return False

    def generate_ships(self):

        """
        Starts yielding posts shared to this dock chronologically
        """
        for shipid,shipdate in self.sailed_ships:
            yield shipid

    def sail_ship_to_this_dock(self, ship_id):
        self.sailed_ships.append((ship_id, dt.datetime.utcnow()))
        return True

    def sink_ship_from_this_dock(self, ship_id):
        for ship, date_time in self.sailed_ships:
            if ship is ship_id:
                self.sailed_ships.remove((ship, date_time))
                return True
        return False


    def max_reactions_ship(self):
        maxreactions=0
        maxreactions_id=-1
        for ship in self.generate_ships():
            reactions=0
            for key, dictlist in database[ship.id].reactions.items():
                reactions+=len(dictlist)
            if reactions>maxreactions:
                maxreactions=reactions
                maxreactions_id=ship.id
        return maxreactions_id,maxreactions

    def max_comments_ship(self):
        maxcomments=0
        maxcomments_id=-1
        for ship in self.generate_ships():
            if len(database[ship.id].child_ships)>maxcomments:
                maxcomments=len(database[ship.id].child_ships)
                maxcomments_id=ship.id
        return maxcomments_id,maxcomments

    def docks_you_may_know(self):

        """
        Function that generates tuples of (id,matual_friends_no ) of other docks the input-dock doesn't know after
        building a database of docks of friends of friends using graph breadth first traversal
        """
        recommendations = {}
        for friend in self.friends:
            for vertex in database[friend].friends:
                if vertex in recommendations.keys():
                    recommendations[vertex] += 1
                else:
                    recommendations[vertex] = 1

        sorted_recommendations = sorted(recommendations.items(), key=lambda tup: tup[1], reverse=True)

        for recommendation in sorted_recommendations:
            yield recommendation

    def seas_you_might_join(self):

        """
        Function that generates tuples of (id,friends_members_no ) of seas the input-dock hasn't joined after building
        a database of friends's seas using graph breadth first traversal
        """
        recommendations = {}
        for friend in self.friends:
            for group in database[friend].groups:
                if group in recommendations.keys():
                    recommendations[group] += 1
                else:
                    recommendations[group] = 1

        sorted_recommendations = sorted(recommendations.items(), key=lambda tup: tup[1], reverse=True)

        for recommendation in sorted_recommendations:
            yield recommendation

    def newsfeed_ships(self):

        """
        Function that generates ids of ships that was posted to friends' docks and joined
        seas chronologically
        """
        posts = []
        # post is a list of tuples (post_id,post_no_in_sailedships_list)
        for friend in self.friends:
            friend_posts=database[friend].sailed_ships
            no_of_posts=len(friend_posts)
            newest_post_id=friend_posts[no_of_posts-1][0]
            posts.add((newest_post_id,no_of_posts-1))
        for group in self.groups:
            group_posts = database[group].sailed_ships
            no_of_posts = len(group_posts)
            newest_post_id = group_posts[no_of_posts - 1][0]
            posts.add((newest_post_id, no_of_posts - 1))

        sorted_posts = sortedcontainers.SortedListWithKey(posts, key=lambda tup: database[tup[0]].creation_date)

        for post_id, post_no in sorted_posts:
            yield post_id
            sorted_posts.pop()
            if post_no != 0:
                post_creator_id=database[post_id].creator_id
                posts = database[post_creator_id].sailed_ships
                new_post_id=posts[post_no-1][0]
                sorted_posts((new_post_id,post_no-1))


    @staticmethod
    def import_from_database(line):
        loaded_personal_dock = PersonalDock()
        return loaded_personal_dock

    def export_to_database(self):
        line = str()
        return line

    def export_to_xml(self):
        pass
