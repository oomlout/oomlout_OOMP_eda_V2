
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ61"
    hexID = "SZKCNRJ61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8P8C', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ61', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '8P8C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 8P8C (8 positions 8 connected)', 'kicadSymbolki_fp_filters': '8P8C* RJ31* RJ32* RJ33* RJ34* RJ35* RJ41* RJ45* RJ49* RJ61*'}])
    newPart['name'].append('RJ61')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

