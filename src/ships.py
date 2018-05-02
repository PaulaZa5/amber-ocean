"""
This file contains all ships related operations
"""

import amber
from amber import AmberObject
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
        return new.id

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
        self.reactions = {}  # id: reaction
        self.parent_ship_id = parent_ship_id
        self.creation_date = dt.datetime.utcnow().replace(microsecond=0)
        self.child_ships = []
        self.edit_history = []  # Tuples of four elements (text content, image content, video content, creation date)

    def add_reply(self, replyer_id, reply_type, reply_text, reply_image=None, reply_video=None):
        Ship.RegisterShip(replyer_id, self.where_is_it_created_id, reply_type, reply_text,
                          reply_image, reply_video, ShipPrivacy.Everyone, self.id)
        self.child_ships.append(str(AmberObject.current_available_id-1))
        return True

    def change_reaction(self, reactioner_id, new_reaction):
        self.reactions[reactioner_id] = new_reaction
        return True

    def remove_reaction(self, reactioner_id):
        del self.reactions[reactioner_id]
        return True

    def count_of_reaction(self, reaction):
        result = 0
        for user_id, saved_reaction in self.reactions.items():
            if saved_reaction == reaction:
                result = result + 1
        return result

    def commit_edit(self, edit_text, edit_image=None, edit_video=None):
        self.edit_history.append((self.txt_content, self.image_content, self.video_content, self.creation_date))
        self.txt_content = edit_text
        self.image_content = edit_image
        self.video_content = edit_video
        self.creation_date = dt.datetime.utcnow().replace(microsecond=0)
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
        loadedShip = Ship("", "", "", "", new_object=False)
        for line in lines:
            attribute = line[0:line.find("\t")]
            attributeValue = line[line.find("\t") + 1:line.find("\n")]
            if attributeValue == "True":
                loadedShip.attribute = True
            elif attributeValue == "False":
                loadedShip.attribute = False
            elif  (attributeValue.find(":") != -1) and attribute=='reactions':
                line = line.replace("reactions\t", "")
                dictlines = line.split(";")
                for dictline in dictlines:
                    dictlist = dictline.split(":")
                    valueslist = dictlist[1].split(",")
                    if not (valueslist[0] == '\n'):
                        loadedShip.reactions[dictlist[0]] = valueslist
            elif not (attributeValue.find("(") == -1):
                tuplesvalue = [tuple(i for i in element.strip('()').split(',')) for element in
                               attributeValue.split('),(')]
                for i in range(len(tuplesvalue)):
                    for j in range(len(tuplesvalue[i])):
                        if "datetime.datetime" in tuplesvalue[i][j]:
                            tupvalue = tuplesvalue[i][j].replace('datetime.datetime', '')
                            date = dt.datetime.strptime(tupvalue, f)
                            tuplesvalue[i] = list(tuplesvalue[i])
                            tuplesvalue[i][j] = date
                            tuplesvalue[i] = tuple(tuplesvalue[i])
                setattr(loadedShip, attribute, tuplesvalue)
            elif not (attributeValue.find(",") == -1):
                listvalue = attributeValue.split(',')
                setattr(loadedShip, attribute, listvalue)
            else:
                if "datetime.datetime" in attributeValue:
                    attributeValue=attributeValue.replace('datetime.datetime','')
                    date = dt.datetime.strptime(attributeValue, f)
                    setattr(loadedShip, attribute, date)
                else:
                    setattr(loadedShip, attribute, attributeValue)

        return loadedShip

    def export_to_database(self):
        line = str()
        for attribute, attributeValue in vars(self).items():
            if attribute == "id" or attributeValue == None:
                continue
            if not (isinstance(attributeValue, bool)) and not (isinstance(attributeValue, dt.date)):
                if len(attributeValue) == 0:
                    continue
            line += "<" + attribute + ">"

            if type(attributeValue) is dict:
                line += "\n" + "\t"
                for key, dictlist in attributeValue.items():

                    line += key + ":"
                    for value in dictlist:
                        line += str(value) + ","
                    if line[len(line) - 1] == ",":
                        line = line[:-1]  # to remove the last "," in the line
                    line += ";"
                if line[len(line) - 1] == ";":
                    line = line[:-1]  # to remove the last ";" in the line
            elif type(attributeValue) is list:
                line += "\n" + "\t"
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
                attrstring = str(attributeValue)
                if isinstance(attributeValue, dt.datetime):
                    attrstring = "datetime.datetime" + attrstring
                line += "\n" + "\t" + attrstring

            line += "\n" + "</" + attribute + ">" + "\n"
        return line

    @staticmethod
    def load_from_xml(location='ship.xml', creator_id="", destination_id=""):
        import xml.etree.ElementTree as et
        ship = et.parse(location)
        ship_data = ship.getroot()
        ship = amber.database[Ship.RegisterShip(creator_id, destination_id, ship_data.attrib['Type'], None, None, None,
                                                ship_data.attrib['Privacy'])]
        ship.creation_date = dt.datetime.strptime(ship_data.attrib['Creation-Time'], '%Y-%m-%d %H:%M:%S')

        for elem in ship_data:
            if elem.tag == "Image":
                ship.image_content = elem.text
            elif elem.tag == "Text":
                ship.txt_content = elem.text
            elif elem.tag == "Video":
                ship.video_content = elem.text

        return ship.id

    def export_to_xml(self, destination='ship.xml', to_file=True):
        import xml.etree.ElementTree as et
        data = et.Element('Ship')
        data.set('Creation-Time', str(self.creation_date))
        try:
            data.set('Creator', amber.database[self.creator_id].name)
        except:
            pass
        try:
            data.set('Destination', amber.database[self.where_is_it_created_id].name)
        except:
            pass
        data.set('Privacy', self.privacy)
        data.set('Type', self.content_type)

        if self.content_type == ContentType.Image:
            img = et.SubElement(data, 'Image')
            img.text = self.image_content
        react = et.SubElement(data, 'Reactions')
        angry = et.SubElement(react, 'Angry')
        for id in self.reactions[Reactions.Angry]:
            angry.text = angry.text + ", " + amber.database[id].name
        dislike = et.SubElement(react, 'Dislike')
        for id in self.reactions[Reactions.Dislike]:
            dislike.text = dislike.text + ", " + amber.database[id].name
        haha = et.SubElement(react, 'Haha')
        for id in self.reactions[Reactions.Haha]:
            haha.text = haha.text + ", " + amber.database[id].name
        like = et.SubElement(react, 'Like')
        for id in self.reactions[Reactions.Like]:
            like.text = like.text + ", " + amber.database[id].name
        love = et.SubElement(react, 'Love')
        for id in self.reactions[Reactions.Love]:
            love.text = love.text + ", " + amber.database[id].name
        txt = et.SubElement(data, 'Text')
        txt.text = self.txt_content
        if self.content_type == ContentType.Video:
            vid = et.SubElement(data, 'Video')
            vid.text = self.video_content

        if to_file:
            xmlfile = open(destination, "w")
            xmlfile.write(et.tostring(data).decode().replace('>, ', '>'))
            xmlfile.close()

        return data
