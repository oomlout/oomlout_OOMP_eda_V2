
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "A1301EUA-T"
    hexID = "SZKSENMAGNETICA131EUAT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1301KUA-T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1301EUA-T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1301-2-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'Linear Hall Effect Sensor, SIP 3pin'}])
    newPart['name'].append('A1301EUA-T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

