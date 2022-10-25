
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "pspice"
    oIndex = "ISOURCE"
    hexID = "SZKPSPICEISOURCE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'I', 'kicadSymbolValue': 'ISOURCE', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Current source symbol for simulation only'}])
    newPart['name'].append('pspice : ISOURCE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

