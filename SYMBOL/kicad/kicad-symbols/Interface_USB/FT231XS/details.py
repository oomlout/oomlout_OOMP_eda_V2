
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT231XS"
    hexID = "SZKINTERFACEUFT231XS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT231XS', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT231X.pdf', 'kicadSymbolki_keywords': 'FTDI USB UART interface converter', 'kicadSymbolki_description': 'Full Speed USB to Full Handshake UART, SSOP-20', 'kicadSymbolki_fp_filters': '*SSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Interface_USB : FT231XS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

