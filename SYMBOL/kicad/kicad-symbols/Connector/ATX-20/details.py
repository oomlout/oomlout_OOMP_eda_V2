
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "ATX-20"
    hexID = "SZKCNATX2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'ATX-20', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://web.aub.edu.lb/pub/docs/atx_201.pdf#page=20', 'kicadSymbolki_keywords': 'ATX PSU', 'kicadSymbolki_description': 'ATX Power supply 20pins', 'kicadSymbolki_fp_filters': '*Mini?Fit*2x10*Vertical* *Mini?Fit*2x10*Horizontal*'}])
    newPart['name'].append('Connector : ATX-20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

