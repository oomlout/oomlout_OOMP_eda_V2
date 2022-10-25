
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Mechanical"
    oIndex = "Housing_Pad"
    hexID = "SZKMECHANICALHOUSINGPAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'N', 'kicadSymbolValue': 'Housing_Pad', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'housing enclosure shield', 'kicadSymbolki_description': 'Housing with connection pin'}])
    newPart['name'].append('Mechanical : Housing_Pad')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

