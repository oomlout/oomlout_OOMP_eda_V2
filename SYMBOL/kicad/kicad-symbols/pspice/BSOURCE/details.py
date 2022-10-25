
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "pspice"
    oIndex = "BSOURCE"
    hexID = "SZKPSPICEBSOURCE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'B', 'kicadSymbolValue': 'BSOURCE', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ltwiki.org/?title=B_sources_%28complete_reference%29', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Arbitrary behavioral voltage or current source'}])
    newPart['name'].append('pspice : BSOURCE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

