
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SC16IS762IBS"
    hexID = "SZKINTERFACEUARTSC16IS762IBS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SC16IS752IBS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC16IS762IBS', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SC16IS752_SC16IS762.pdf', 'kicadSymbolki_keywords': 'UART I2C/SPI 64B FIFO IrDA SIR', 'kicadSymbolki_description': 'Dual UART with I2C/SPI interface, 64 bytes of transmit and receive FIFOs, IrDA SIR built-in support, HVQFN-32', 'kicadSymbolki_fp_filters': 'VQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Interface_UART : SC16IS762IBS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

