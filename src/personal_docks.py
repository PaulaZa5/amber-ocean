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
        return new.id

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
        self.join_date = dt.datetime.utcnow().replace(microsecond=0)

    def check_password(self, password):
        password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        return  self.password == password

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
        old_master_email=self.master_email
        self.master_email = new_email
        check=self.remove_email( old_master_email)
        self.add_email(self.master_email)
        return check

    def add_email(self, new_email):
        self.emails.append(new_email)
        return True

    def remove_email(self, email):
        if email in self.emails:
            if email!=self.master_email:
                self.emails.remove(email)
                return True
            else:
                return False
        else:
            return False

    def change_master_phone_number(self, new_phone_number):
        old_master_phone_number = self.master_phone_number
        self.master_phone_number = new_phone_number
        self.add_phone_number( self.master_phone_number)
        check = self.remove_phone_number(old_master_phone_number)
        return check

    def add_phone_number(self, new_phone_number):
        self.phone_numbers.append(new_phone_number)
        return True

    def remove_phone_number(self, phone_number):
        if phone_number in self.phone_numbers:
            if phone_number!=self.master_phone_number:
                self.phone_numbers.remove(phone_number)
                return True
            else:
                return False
        else:
            return False

    def add_friend(self, friend_id):
        self.friends.append(friend_id)
        return True

    def remove_friend(self, friend_id):
        if friend_id in self.friends:
            self.friends.remove(friend_id)
            return True
        return False

    def add_follower(self, follower_id):
        self.followers.append(follower_id)
        return True

    def remove_follower(self, follower_id):
        if follower_id in self.followers:
            self.followers.remove(follower_id)
            return True
        else:
            return False

    def add_followee(self, followee_id):
        self.followees.append(followee_id)
        return True

    def remove_followee(self, followee_id):
        if followee_id in self.followees:
            self.followees.remove(followee_id)
            return True
        else:
            return False

    def add_family_member_relationship(self, family_member_id, family_member_relation):
        self.family.append((family_member_id, family_member_relation))
        return True

    def edit_family_member_relationship(self, family_member_id, new_family_member_relation):
        exist=self.remove_family_member_relationship( family_member_id)
        if exist:
            self.add_family_member_relationship( family_member_id, new_family_member_relation)
        return exist

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
        exist = self.remove_education( major, place_of_education)
        if exist:
            self.add_education( major, place_of_education, new_starting_date, new_finishing_date)
        return exist

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
        exist = self.remove_living_place( location)
        if exist:
            self.add_living_place( location, new_starting_date, new_finishing_date)
        return exist

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
        exist = self.remove_relationship( significant_other_id)
        if exist:
            self.add_relationship( significant_other_id, new_type, new_starting_date, new_finishing_date)
        return exist

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
        exist = self.remove_link( new_link_url)
        if exist:
            self.add_link( link_string, new_link_url)
        return exist

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
        exist = self.remove_special_field( special_field_string)
        if exist:
            self.add_special_field( special_field_string, new_special_field_text)
        return exist

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

    def join_sea(self,sea_id):
        self.seas.append(sea_id)

    def leave_sea(self,sea_id):
        if sea_id in self.seas:
            self.seas.remove(sea_id)
            return True
        else:
            return False

    def max_reactions_ship(self):
        maxreactions=0
        maxreactions_id=-1
        for ship in self.generate_ships():
            reactions=0
            for key, dictlist in database[ship].reactions.items():
                reactions+=len(dictlist)
            if reactions>maxreactions:
                maxreactions=reactions
                maxreactions_id=ship
        return maxreactions_id,maxreactions

    def max_comments_ship(self):
        maxcomments=0
        maxcomments_id=-1
        for ship in self.generate_ships():
            if len(database[ship].child_ships)>maxcomments:
                maxcomments=len(database[ship].child_ships)
                maxcomments_id=ship
        return maxcomments_id,maxcomments

    def docks_you_may_know(self):

        """
        Function that generates tuples of (id,matual_friends_no ) of other docks the input-dock doesn't know after
        building a database of docks of friends of friends using graph breadth first traversal
        """
        recommendations = {}
        for friend in self.friends:
            for vertex in database[friend].friends:
                if vertex!=self.id and not( vertex in self.friends):
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
            for group in database[friend].seas:
                if not (group in self.seas):
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
            if no_of_posts!=0:
                newest_post_id=friend_posts[no_of_posts-1][0]
                posts.append((newest_post_id,no_of_posts-1))
        for group in self.seas:
            group_posts = database[group].sailed_ships
            no_of_posts = len(group_posts)
            if no_of_posts != 0:
                newest_post_id = group_posts[no_of_posts - 1][0]
                posts.append((newest_post_id, no_of_posts - 1))
        sorted_posts = sortedcontainers.SortedListWithKey(posts, key=lambda tup: database[tup[0]].creation_date)
        for post_id, post_no in sorted_posts:
            yield post_id
            if post_no != 0:
                post_creator_id=database[post_id].creator_id
                posts = database[post_creator_id].sailed_ships
                new_post_id=posts[post_no-1][0]
                sorted_posts.add((new_post_id,post_no-1))

    @staticmethod
    def import_from_database(inData):
        f = "%Y-%m-%d %H:%M:%S"
        lines = inData.split('>\n')
        file = open('dataout.xml', 'w')
        for line in lines:
            line = line.replace('>', '')
            if not (line.find("</") == -1):
                line = line.replace("</" + temp, '')
            else:
                line = line.replace('<', '')
                temp = line
            file.write(line)
        file.close()
        file = open('dataout.xml', 'r')
        lines = iter(file.readlines())
        loadedDock = PersonalDock("", "", "", "", new_object=False)
        for line in lines:
            attribute = line[0:line.find("\t")]
            attributeValue = line[line.find("\t") + 1:line.find("\n")]
            if attributeValue == "True":
                loadedDock.attribute = True
            elif attributeValue == "False":
                loadedDock.attribute = False
            elif not (attributeValue.find("(") == -1):
                tuplesvalue = [tuple(i for i in element.strip('()').split(',')) for element in attributeValue.split('),(')]
                for i in range(len(tuplesvalue)):
                    for j in range(len(tuplesvalue[i])):
                        if  "datetime.datetime" in tuplesvalue[i][j]:
                            tupvalue=tuplesvalue[i][j].replace('datetime.datetime','')
                            date=dt.datetime.strptime(tupvalue, f)
                            tuplesvalue[i]=list(tuplesvalue[i])
                            tuplesvalue[i][j]=date
                            tuplesvalue[i]=tuple(tuplesvalue[i])
                setattr(loadedDock, attribute, tuplesvalue)
            elif not (attributeValue.find(",") == -1):
                listvalue = attributeValue.split(',')
                setattr(loadedDock, attribute, listvalue)

            else:
                if "datetime.datetime" in attributeValue:
                    attributeValue=attributeValue.replace('datetime.datetime','')
                    date = dt.datetime.strptime(attributeValue, f)
                    setattr(loadedDock, attribute, date)
                else:
                    setattr(loadedDock, attribute, attributeValue)

        return loadedDock

    def export_to_database(self):
        line = str()
        for attribute, attributeValue in vars(self).items():
            if attribute == "id" or attributeValue == None:
                continue
            if not (isinstance(attributeValue, bool)) and not (isinstance(attributeValue, dt.date)):
                if len(attributeValue) == 0:
                    continue
            line += "<" + attribute + ">"
            line += "\n" + "\t"
            if type(attributeValue) is list:
                for value in attributeValue:
                    if type(value) is tuple:
                        line += "("

                        for x in value:
                            attrstring = str(x)
                            if isinstance(x, dt.datetime):
                                attrstring = "datetime.datetime" + attrstring
                            line += attrstring +","

                        line = line[:-1]  # to remove the last "," in the line
                        line += "),"
                    else:
                        line += str(value) + ","
                if line[len(line) - 1] == ",":
                    line = line[:-1]  # to remove the last "," in the line
            else:
                attrstring=str(attributeValue)
                if isinstance(attributeValue, dt.datetime):
                    attrstring="datetime.datetime"+attrstring
                line += attrstring

            line += "\n" + "</" + attribute + ">" + "\n"
        return line

    @staticmethod
    def load_from_xml(location='personaldock.xml'):
        import xml.etree.ElementTree as et
        dock = et.parse(location)
        dock_data = dock.getroot()
        dock = PersonalDock.RegisterAccount(dock_data.attrib['Name'], dock_data.attrib['Gender'],
                                            dt.datetime.strptime(dock_data.attrib['Birthday'], '%Y-%m-%d %H:%M:%S'),
                                            '0', dock_data.attrib['Master-Email'],
                                            dock_data.attrib['Master-Phone-Number'])
        dock.join_date = dt.datetime.strptime(dock_data.attrib['Join-Date'], '%Y-%m-%d %H:%M:%S')
        if dock_data.attrib['Active'] == 'False':
            dock.active = False
        dock.password = dock_data.attrib['Hashed-Password']
        dock.relationship_status = dock_data.attrib['Relationship-Status']
        dock.emails = []
        dock.phone_numbers = []

        for elem in dock_data:
            if elem.tag == "Education":
                for ed in elem:
                    dock.add_education(ed.attrib['Major'], ed.attrib['Place'],
                                       dt.datetime.strptime(ed.attrib['Start-Date'], '%Y-%m-%d %H:%M:%S'),
                                       dt.datetime.strptime(ed.attrib['Finishing-Date'], '%Y-%m-%d %H:%M:%S'))
            elif elem.tag == "Emails":
                for email in elem:
                    dock.add_email(email.attrib['Email'])
            elif elem.tag == "Links":
                for link in elem:
                    link_s, url = tuple(list(link.attrib.items())[0])
                    dock.add_link(link_s, url)
            elif elem.tag == "Living-Places":
                for place in elem:
                    dock.add_living_place(place.attrib['Place'],
                                          dt.datetime.strptime(ed.attrib['Start-Date'], '%Y-%m-%d %H:%M:%S'),
                                          dt.datetime.strptime(ed.attrib['Finishing-Date'], '%Y-%m-%d %H:%M:%S'))
            elif elem.tag == "Phone-Numbers":
                for ph_n in elem:
                    dock.add_phone_number(ph_n.attrib['Number'])
            elif elem.tag == "Special-Fields":
                for field in elem:
                    field_s, field_d = tuple(list(field.attrib.items())[0])
                    dock.add_special_field(field_s, field_d)

        return dock.id

    def export_to_xml(self, destination='personaldock.xml', to_file=True):
        import xml.etree.ElementTree as et
        data = et.Element('Personal-Dock')
        data.set("Active", str(self.active))
        data.set('Birthday', str(self.birthday))
        data.set('Gender', self.gender)
        data.set('Hashed-Password', self.password)
        data.set('Join-Date', str(self.join_date))
        data.set('Master-Email', self.master_email)
        data.set('Master-Phone-Number', self.master_phone_number)
        data.set('Name', self.name)
        data.set("Relationship-Status", self.relationship_status)

        educat = et.SubElement(data, 'Education')
        for num, ed in enumerate(self.education):
            major, place, start, end = ed
            n_ed = et.SubElement(educat, "Education" + str(num + 1))
            n_ed.set("Major", major)
            n_ed.set("Place", place)
            n_ed.set("Start-Date", str(start))
            n_ed.set("Finishing-Date", str(end))
        emails = et.SubElement(data, 'Emails')
        for num, email in enumerate(self.emails):
            n_email = et.SubElement(emails, "Email" + str(num + 1))
            n_email.set("Email", email)
        fam_mem = et.SubElement(data, 'Family-Members')
        for num, rel in enumerate(self.family):
            mem_id, relationship = rel
            n_relationship = et.SubElement(fam_mem, "Relationship" + str(num + 1))
            n_relationship.set("Family-Member", amber.database[mem_id].name)
            n_relationship.set("Relationship", relationship)
        followees = et.SubElement(data, 'Followees')
        followees.text = ""
        for followee in self.followees:
            followees.text = followees.text + ", " + amber.database[followee].name
        followers = et.SubElement(data, 'Followers')
        followers.text = ""
        for follower in self.followers:
            followers.text = followers.text + ", " + amber.database[follower].name
        friends = et.SubElement(data, 'Friends')
        friends.text = ""
        for friend in self.friends:
            friends.text = friends.text + ", " + amber.database[friend].name
        links = et.SubElement(data, 'Links')
        for num, link in enumerate(self.links):
            string, url = link
            n_link = et.SubElement(links, "Link" + str(num + 1))
            n_link.set(string, url)
        liv_in = et.SubElement(data, 'Living-Places')
        for num, place_data in enumerate(self.living_in):
            place, start, end = place_data
            n_li = et.SubElement(liv_in, "Living-Place" + str(num + 1))
            n_li.set("Place", place)
            n_li.set("Start-Date", str(start))
            n_li.set("Finishing-Date", str(end))
        phone_numbers = et.SubElement(data, 'Phone-Numbers')
        for num, phone_no in enumerate(self.phone_numbers):
            n_phone = et.SubElement(phone_numbers, "Phone-Number" + str(num + 1))
            n_phone.set("Number", phone_no)
        so_relationships = et.SubElement(data, 'Relationships')
        for num, rel in enumerate(self.relationships):
            mem_id, type, start, end = rel
            n_relationship = et.SubElement(so_relationships, "Relationship" + str(num + 1))
            n_relationship.set("Significant-Other", amber.database[mem_id].name)
            n_relationship.set("Type", type)
            n_relationship.set("Start", str(start))
            n_relationship.set("End", str(end))
        joined_seas = et.SubElement(data, 'Seas')
        joined_seas.text = ""
        for sea in self.seas:
            joined_seas.text = joined_seas.text + ", " + amber.database[sea].name
        sp_fields = et.SubElement(data, 'Special-Fields')
        for num, field in enumerate(self.special_fields):
            string, desc = field
            n_field = et.SubElement(sp_fields, "Field" + str(num + 1))
            n_field.set(string, desc)

        if to_file:
            xmlfile = open(destination, "w")
            xmlfile.write(et.tostring(data).decode().replace('>, ', '>'))
            xmlfile.close()

        return True
