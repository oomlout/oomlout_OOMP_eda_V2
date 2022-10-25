
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_WallPlug_Earth"
    hexID = "SZKCNCONNWALLPLUGEARTH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'P', 'kicadSymbolValue': 'Conn_WallPlug_Earth', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'wall plug 110VAC 220VAC', 'kicadSymbolki_description': '3-pin general wall plug, with Earth wire (110VAC, 220VAC)'}])
    newPart['name'].append('Connector : Conn_WallPlug_Earth')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

