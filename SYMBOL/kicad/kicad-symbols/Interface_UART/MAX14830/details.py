
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX14830"
    hexID = "SZKINTERFACEUARTMAX1483"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX14830', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-48-1EP_7x7mm_P0.5mm_EP5.1x5.1mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX14830.pdf', 'kicadSymbolki_keywords': 'UART I2C/SPI 128W FIFO IrDA SIR', 'kicadSymbolki_description': 'Quad UART with I2C/SPI interface, 128 Word FIFOs, IrDA SIR built-in support, TQFN-48', 'kicadSymbolki_fp_filters': 'TQFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Interface_UART : MAX14830')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

