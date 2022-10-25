
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_Arrow45_XLarge"
    hexID = "SZKGRAPHICSYMARROW45XL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_Arrow45_XLarge', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'symbol arrow 45° angled', 'kicadSymbolki_description': 'Filled 45° arrow, 400mil'}])
    newPart['name'].append('Graphic : SYM_Arrow45_XLarge')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

