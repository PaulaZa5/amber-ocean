'''personalDock'''
def import_from_database():
    file = open('dataDock.xml','r')
    lines =file.read().split('>\n')
    file.close()
    file = open('dataout.xml', 'w')
    for line in lines:
        line=line.replace('>','')
        if not(line.find("</")==-1):
             line=line.replace("</"+temp, '')
        else:
            line=line.replace('<', '')
            temp=line
        file.write(line)
    file.close()
    file = open('dataout.xml', 'r')
    lines = iter(file.readlines())
    loadedDock=PersonalDock("","","","")
    for line in lines:
        attribute = line[0:line.find("\t")]
        attributeValue=line[line.find("\t")+1:line.find("\n")]
        if attributeValue=="True":
            loadedDock.attribute=True
        elif attributeValue=="False":
            loadedDock.attribute = False
        elif not (attributeValue.find("(") == -1):
            tuplesvalue=[tuple(i for i in element.strip('()').split(',')) for element in attributeValue.replace(' ','').split('),(')]
            setattr(loadedDock, attribute, tuplesvalue)
        elif not (attributeValue.find(",")==-1):
            listvalue=attributeValue.split(',')
            setattr(loadedDock, attribute, listvalue)

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
        line+="<"+attribute+">"
        line += "\n" + "\t"
        if type(attributeValue) is list:
            for value in attributeValue:
                if type(value) is tuple:
                    line += "("

                    for x in value:
                        line += str(x) + ","

                    line = line[:-1]  # to remove the last "," in the line
                    line += "),"
                else:
                    line += str(value) + ","
            if line[len(line) - 1] == ",":
                line = line[:-1]  # to remove the last "," in the line
        else:
            line+=str(attributeValue)

        line+="\n"+"</"+attribute+">"+"\n"
    return line
'''ship'''
def import_from_database():
    file = open('dataShip.xml', 'r')
    lines = file.read().split('>\n')
    file.close()
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
    loadedShip = Ship("", "", "")
    for line in lines:
        attribute = line[0:line.find("\t")]
        attributeValue = line[line.find("\t") + 1:line.find("\n")]
        if attributeValue == "True":
            loadedShip.attribute = True
        elif attributeValue == "False":
            loadedShip.attribute = False
        elif not (attributeValue.find(":") == -1):
            line=line.replace("reactions\t","")
            dictlines=line.split(";")
            for dictline in dictlines:
                dictlist=dictline.split(":")
                valueslist=dictlist[1].split(",")
                if not(valueslist[0]=='\n'):
                    loadedShip.reactions[dictlist[0]]=valueslist
        elif not (attributeValue.find("(") == -1):
            tuplesvalue = [tuple(i for i in element.strip('()').split(',')) for element in
                           attributeValue.replace(' ', '').split('),(')]
            setattr(loadedShip, attribute, tuplesvalue)
        elif not (attributeValue.find(",") == -1):
            listvalue = attributeValue.split(',')
            setattr(loadedShip, attribute, listvalue)


        else:
            setattr(loadedShip, attribute, attributeValue)

    return loadedShip

def export_to_database(self):
    line = str()
    for attribute, attributeValue in vars(self).items():
        if attribute == "id" or attributeValue == None:
            continue
        if not(isinstance(attributeValue, bool)) and not(isinstance(attributeValue,dt.date)):
            if len(attributeValue) == 0:
             continue
        line += "<" + attribute + ">"

        if type(attributeValue) is dict:
            line += "\n" + "\t"
            for key,dictlist in attributeValue.items():

                line += key+":"
                for value in dictlist:
                    line += str(value) + ","
                if line[len(line)-1]==",":
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
                        line += str(x) + ","

                    line = line[:-1]  # to remove the last "," in the line
                    line += "),"
                else:
                    line += str(value)+","
            if line[len(line) - 1] == ",":
                line = line[:-1]  # to remove the last "," in the line
        else:
            line +="\n"+"\t"+ str(attributeValue)

        line += "\n" + "</" + attribute + ">" + "\n"
    return line
'''sea'''
def import_from_database():
    file = open('dataSea.xml', 'r')
    lines = file.read().split('>\n')
    file.close()
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
    loadedSea = Sea("", "", "")
    for line in lines:
        attribute = line[0:line.find("\t")]
        attributeValue = line[line.find("\t") + 1:line.find("\n")]
        if attributeValue == "True":
            loadedSea.attribute = True
        elif attributeValue == "False":
            loadedSea.attribute = False
        elif not (attributeValue.find("(") == -1):
            tuplesvalue = [tuple(i for i in element.strip('()').split(',')) for element in
                           attributeValue.replace(' ', '').split('),(')]
            setattr(loadedSea, attribute, tuplesvalue)
        elif not (attributeValue.find(",") == -1):
            listvalue = attributeValue.split(',')
            setattr(loadedSea, attribute, listvalue)

        else:
            setattr(loadedSea, attribute, attributeValue)

    return loadedSea

def export_to_database(self):
    line = str()
    for attribute, attributeValue in vars(self).items():
        if attribute == "id" or attributeValue == None:
            continue
        if not(isinstance(attributeValue, bool)) and not(isinstance(attributeValue,dt.date)):
            if len(attributeValue) == 0:
             continue
        line += "<" + attribute + ">"
        line += "\n" + "\t"
        if type(attributeValue) is list:
            for value in attributeValue:
                if type(value) is tuple:
                    line += "("

                    for x in value:
                        line += str(x) + ","

                    line = line[:-1]  # to remove the last "," in the line
                    line += "),"
                else:
                    line += str(value) + ","
            if line[len(line) - 1] == ",":
                line = line[:-1]  # to remove the last "," in the line
        else:
            line += str(attributeValue)

        line += "\n" + "</" + attribute + ">" + "\n"
    return line
