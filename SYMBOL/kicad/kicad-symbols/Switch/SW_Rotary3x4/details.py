
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Rotary3x4"
    hexID = "SZKSWITCHSWROTARY3X4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Rotary3x4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/C200/DS-Serie%23LOR.pdf', 'kicadSymbolki_keywords': 'rotary switch', 'kicadSymbolki_description': '3 rotary switches with 4 positions'}])
    newPart['name'].append('Switch : SW_Rotary3x4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

