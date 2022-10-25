
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_LASER_Large"
    hexID = "SZKGRAPHICSYMLASERL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_LASER_Large', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'symbol logo laser warning', 'kicadSymbolki_description': 'Laser radiation warning symbol, large'}])
    newPart['name'].append('Graphic : SYM_LASER_Large')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

