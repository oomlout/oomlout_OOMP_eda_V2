
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx_IEEE"
    oIndex = "7407"
    hexID = "SZK74XXIEEE747"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '7407', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ''}])
    newPart['name'].append('74xx_IEEE : 7407')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

