
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SC16IS750xBS"
    hexID = "SZKINTERFACEUARTSC16IS75XBS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC16IS750xBS', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-24-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SC16IS740_750_760.pdf', 'kicadSymbolki_keywords': 'UART I2C/SPI 64B FIFO IrDA SIR', 'kicadSymbolki_description': 'Single UART with I2C/SPI interface, 64 bytes of transmit and receive FIFOs, IrDA SIR built-in support, HVQFN-24', 'kicadSymbolki_fp_filters': 'HVQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('SC16IS750xBS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

