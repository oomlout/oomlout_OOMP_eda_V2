
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "LEMO2"
    hexID = "SZKCNLEMO2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'LEMO2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'LEMO connector', 'kicadSymbolki_description': '2-pin LEMO connector'}])
    newPart['name'].append('Connector : LEMO2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

