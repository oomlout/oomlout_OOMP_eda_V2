
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Rotary12"
    hexID = "SZKSWITCHSWROTARY12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Rotary12', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/C200/DS-Serie%23LOR.pdf', 'kicadSymbolki_keywords': 'rotary switch', 'kicadSymbolki_description': 'rotary switch with 12 positions'}])
    newPart['name'].append('SW_Rotary12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

