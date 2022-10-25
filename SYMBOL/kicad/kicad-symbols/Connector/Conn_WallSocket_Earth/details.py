
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_WallSocket_Earth"
    hexID = "SZKCNCONNWALLSOEARTH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_WallSocket_Earth', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'wall socket 110VAC 220VAC', 'kicadSymbolki_description': '3-pin german wall socket, with Earth wire (110VAC, 220VAC)'}])
    newPart['name'].append('Connector : Conn_WallSocket_Earth')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

