
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "Z8530"
    hexID = "SZKINTERFACEUARTZ853"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Z8530', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'SCC Serial Communication', 'kicadSymbolki_description': 'SCC Serial Communication Controller, DIP-40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('Interface_UART : Z8530')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

