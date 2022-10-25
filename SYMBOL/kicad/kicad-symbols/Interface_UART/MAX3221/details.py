
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3221"
    hexID = "SZKINTERFACEUARTMAX3221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3221', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/max3221.pdf', 'kicadSymbolki_keywords': 'serial UART RS232', 'kicadSymbolki_description': 'RS232 transceiver with 15kV ESD protection', 'kicadSymbolki_fp_filters': 'SSOP* TSSOP*'}])
    newPart['name'].append('Interface_UART : MAX3221')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

