
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SC16IS762IPW"
    hexID = "SZKINTERFACEUARTSC16IS762IPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SC16IS752IPW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC16IS762IPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SC16IS752_SC16IS762.pdf', 'kicadSymbolki_keywords': 'UART I2C/SPI 64B FIFO IrDA SIR', 'kicadSymbolki_description': 'Dual UART with I2C/SPI interface, 64 bytes of transmit and receive FIFOs, IrDA SIR built-in support, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : SC16IS762IPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

