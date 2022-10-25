
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "4P2C_Shielded"
    hexID = "SZKCN4P2CSHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': '4P2C_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '4P2C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 4P2C (4 positions 2 connected), Shielded', 'kicadSymbolki_fp_filters': '4P2C*'}])
    newPart['name'].append('Connector : 4P2C_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

