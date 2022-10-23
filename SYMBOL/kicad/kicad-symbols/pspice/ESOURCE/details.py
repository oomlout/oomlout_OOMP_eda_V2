
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "pspice"
    oIndex = "ESOURCE"
    hexID = "SZKPSPICEESOURCE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'E', 'kicadSymbolValue': 'ESOURCE', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.pspice.com/source/controlled-sources', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Voltage-dependent Voltage source symbol for simulation only'}])
    newPart['name'].append('ESOURCE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

