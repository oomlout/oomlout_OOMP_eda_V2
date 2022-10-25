
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_ESD_Small"
    hexID = "SZKGRAPHICSYMESDSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_ESD_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'symbol ESD', 'kicadSymbolki_description': 'ESD warning/"Do not touch" symbol, small'}])
    newPart['name'].append('Graphic : SYM_ESD_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

