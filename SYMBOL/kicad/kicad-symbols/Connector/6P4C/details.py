
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "6P4C"
    hexID = "SZKCN6P4C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': '6P4C', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P4C (6 positions 4 connected), RJ13/RJ14', 'kicadSymbolki_fp_filters': '6P4C* RJ13* RJ14*'}])
    newPart['name'].append('Connector : 6P4C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

