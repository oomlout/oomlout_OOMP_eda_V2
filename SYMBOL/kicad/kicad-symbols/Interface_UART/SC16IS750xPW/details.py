
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SC16IS750xPW"
    hexID = "SZKINTERFACEUARTSC16IS75XPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC16IS750xPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SC16IS740_750_760.pdf', 'kicadSymbolki_keywords': 'UART I2C/SPI 64B FIFO IrDA SIR', 'kicadSymbolki_description': 'Single UART with I2C/SPI interface, 64 bytes of transmit and receive FIFOs, IrDA SIR built-in support, TSSOP-24', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : SC16IS750xPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

