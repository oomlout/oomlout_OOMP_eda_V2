
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "MCP23S17_ML"
    hexID = "SZKINTERFACEEXPANSIONMCP23S17ML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP23S17_ML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_6x6mm_P0.65mm_EP4.25x4.25mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf', 'kicadSymbolki_keywords': 'SPI parallel port expander', 'kicadSymbolki_description': '16-bit I/O expander, SPI, interrupts, w pull-ups, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*6x6mm*P0.65mm*'}])
    newPart['name'].append('Interface_Expansion : MCP23S17_ML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

