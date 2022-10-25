
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "8250"
    hexID = "SZKINTERFACEUART825"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '16450', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8250', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': '1ch UART', 'kicadSymbolki_description': 'PC8250A, Universal Asynchronous Receiver/Transmitter, PDIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface_UART : 8250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

