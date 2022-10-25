
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "pspice"
    oIndex = "INDUCTOR"
    hexID = "SZKPSPICEINDUCTOR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'L', 'kicadSymbolValue': 'INDUCTOR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Inductor symbol for simulation only'}])
    newPart['name'].append('pspice : INDUCTOR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

