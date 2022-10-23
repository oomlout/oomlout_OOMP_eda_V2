
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3218"
    hexID = "SZKINTERFACEUARTMAX3218"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3218', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3218.pdf', 'kicadSymbolki_keywords': '1μA Supply Current', 'kicadSymbolki_description': 'Dual RS-232 Transceiver, 1.8V to 4.25V, AutoShutdown, DIP-20/SSOP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('MAX3218')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

