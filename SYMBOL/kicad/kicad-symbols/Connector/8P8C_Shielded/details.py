
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "8P8C_Shielded"
    hexID = "SZKCN8P8CSHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': '8P8C_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '8P8C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 8P8C (8 positions 8 connected), RJ31/RJ32/RJ33/RJ34/RJ35/RJ41/RJ45/RJ49/RJ61, Shielded', 'kicadSymbolki_fp_filters': '8P8C* RJ31* RJ32* RJ33* RJ34* RJ35* RJ41* RJ45* RJ49* RJ61*'}])
    newPart['name'].append('8P8C_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

