
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "6P2C_Shielded"
    hexID = "SZKCN6P2CSHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': '6P2C_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P2C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P2C (6 positions 2 connected), RJ11, Shielded', 'kicadSymbolki_fp_filters': '6P2C* RJ11*'}])
    newPart['name'].append('Connector : 6P2C_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

