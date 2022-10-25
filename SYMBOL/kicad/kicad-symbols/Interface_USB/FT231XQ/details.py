
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT231XQ"
    hexID = "SZKINTERFACEUFT231XQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT231XQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT231X.pdf', 'kicadSymbolki_keywords': 'FTDI USB UART interface converter', 'kicadSymbolki_description': 'Full Speed USB to Full Handshake UART, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FT231XQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

