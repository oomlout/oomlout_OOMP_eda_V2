
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "A1301KUA-T"
    hexID = "SZKSENMAGNETICA131KUAT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1301KUA-T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1301-2-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'Linear Hall Effect Sensor, SIP 3pin'}])
    newPart['name'].append('Sensor_Magnetic : A1301KUA-T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

