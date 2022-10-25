
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3078E"
    hexID = "SZKINTERFACEUARTMAX378E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SP3481CN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3078E', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3070E-MAX3079E.pdf', 'kicadSymbolki_keywords': 'Low Power Half-Duplex RS-485 RS-422 Transceiver', 'kicadSymbolki_description': '+3.3V, ±15kV ESD-Protected, Fail-Safe, Hot-Swap, RS-485/RS-422 Transceivers, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : MAX3078E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

