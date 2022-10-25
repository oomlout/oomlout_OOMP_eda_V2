
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Mechanical"
    oIndex = "Housing"
    hexID = "SZKMECHANICALHOUSING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'N', 'kicadSymbolValue': 'Housing', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'housing enclosure', 'kicadSymbolki_description': 'Housing', 'kicadSymbolki_fp_filters': 'Enclosure* Housing*'}])
    newPart['name'].append('Mechanical : Housing')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

