
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "pspice"
    oIndex = "GSOURCE"
    hexID = "SZKPSPICEGSOURCE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'G', 'kicadSymbolValue': 'GSOURCE', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.pspice.com/source/controlled-sources', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Voltage-dependent Current source symbol for simulation only'}])
    newPart['name'].append('pspice : GSOURCE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

