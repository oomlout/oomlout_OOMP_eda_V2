
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx_IEEE"
    oIndex = "74LS240"
    hexID = "SZK74XXIEEE74LS24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS240', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74ls240.pdf', 'kicadSymbolki_keywords': '7400 logic ttl low power schottky', 'kicadSymbolki_description': 'Octal Buffer and Line Driver With 3-State Output, active-low enables, inverting outputs'}])
    newPart['name'].append('74xx_IEEE : 74LS240')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

