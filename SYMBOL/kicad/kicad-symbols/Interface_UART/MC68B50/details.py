
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MC68B50"
    hexID = "SZKINTERFACEUARTMC68B5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC6850', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68B50', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/motorola/MC6850.pdf', 'kicadSymbolki_keywords': 'ACIA', 'kicadSymbolki_description': 'Asynchronous Communications Interface Adapter 2MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface_UART : MC68B50')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

