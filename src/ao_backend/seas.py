"""
This file contains all seas related operations
"""
from amber import database
import amber
import datetime as dt


class SeaSailingPrivacy(enumerate):
    Only_administrators = 'onlyadministrators'
    Only_editors = 'onlyeditors'
    Everyone = 'everyone'


class SeaVisibilityPrivacy(enumerate):
    Only_Members = 'onlymembers'
    Everyone = 'everyone'


class Sea(amber.AmberObject):

    """
    Sea class
    """

    @staticmethod
    def RegisterSea(creator, name, description, visibility_privacy=SeaVisibilityPrivacy.Everyone,
                 sailing_privacy=SeaSailingPrivacy.Everyone, new_object=True):
        new = Sea(creator, name, description, visibility_privacy, sailing_privacy, new_object)
        amber.database[new.id] = new
        return new

    def __init__(self, creator, name, description, visibility_privacy=SeaVisibilityPrivacy.Everyone,
                 sailing_privacy=SeaSailingPrivacy.Everyone, new_object=True):
        super().__init__(new_object)
        self.creator = creator
        self.name = name
        self.description = description
        self.visibility_privacy = visibility_privacy
        self.sailing_privacy = sailing_privacy
        self.active = True
        self.administrators = [creator]
        self.editors = []
        self.members = [creator]
        self.sailed_ships = []  # Tuples of two elements (ship id, initial sailing date)
        self.creation_date = dt.datetime.utcnow().now()
        self.creation_date = self.creation_date.replace(microsecond=0)

    def deactivate(self):
        self.active = False
        return True

    def change_name(self, name):
        self.name = name
        return True

    def change_description(self, description):
        self.description = description
        return True

    def is_administrator(self, id):
        return id in self.administrators

    def add_administrator(self, new_administrator_id):
        self.administrators.append(new_administrator_id)
        return True

    def remove_administrator(self, administrator_id):
        self.administrators.remove(administrator_id)
        return True

    def is_editor(self, id):
        return id in self.editors


    def add_editor(self, new_editor_id):
        self.editors.append(new_editor_id)
        return True

    def remove_editor(self, editor_id):
        self.editors.remove(editor_id)
        return True

    def is_member(self, id):
        return id in self.members

    def add_member(self, new_member_id):
        self.members.append(new_member_id)
        return True

    def remove_member(self, member_id):
        self.members.remove(member_id)
        return True

    def change_visibility_privacy(self, new_visibility_privacy):
        self.visibility_privacy = new_visibility_privacy
        return True

    def change_sailing_privacy(self, new_sailing_privacy):
        self.sailing_privacy = new_sailing_privacy
        return True


    def generate_ships(self):
        """
        Starts yielding posts shared to this sea chronologically
        """
        
        for shipid, shipdate in self.sailed_ships:
            yield shipid

    def sail_ship_to_this_sea(self, ship_id):
        self.sailed_ships.append((ship_id , dt.datetime.utcnow().date()))
        return True

    def sink_ship_from_this_sea(self, ship_id):
        for ship,date in self.sailed_ships:
            if ship == ship_id:
                self.sailed_ships.remove(ship)
        return True
      
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
        loadedSea = Sea("", "", "", new_object=False)
        for line in lines:
            attribute = line[0:line.find("\t")]
            attributeValue = line[line.find("\t") + 1:line.find("\n")]
            if attributeValue == "True":
                loadedSea.attribute = True
            elif attributeValue == "False":
                loadedSea.attribute = False
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
                setattr(loadedSea, attribute, tuplesvalue)
            elif not (attributeValue.find(",") == -1):
                listvalue = attributeValue.split(',')
                setattr(loadedSea, attribute, listvalue)

            else:
                if "datetime.datetime" in attributeValue:
                    attributeValue=attributeValue.replace('datetime.datetime','')
                    date = dt.datetime.strptime(attributeValue, f)
                    setattr(loadedSea, attribute, date)
                else:
                    setattr(loadedSea, attribute, attributeValue)

        return loadedSea

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
                attrstring = str(attributeValue)
                if isinstance(attributeValue, dt.datetime):
                    attrstring = "datetime.datetime" + attrstring
                line += attrstring

            line += "\n" + "</" + attribute + ">" + "\n"
        return line
      
    def export_to_xml(self):
        pass
