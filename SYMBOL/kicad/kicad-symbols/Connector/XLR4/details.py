
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "XLR4"
    hexID = "SZKCNXLR4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'XLR4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'xlr connector', 'kicadSymbolki_description': 'XLR Connector, Male or Female, 4 Pins', 'kicadSymbolki_fp_filters': 'Jack*XLR*'}])
    newPart['name'].append('Connector : XLR4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

