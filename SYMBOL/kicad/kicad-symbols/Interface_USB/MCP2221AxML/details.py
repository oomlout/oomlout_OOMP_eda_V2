
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MCP2221AxML"
    hexID = "SZKINTERFACEUMCP2221AXML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2221AxML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005565B.pdf', 'kicadSymbolki_keywords': 'USB I2C UART Converter Bridge', 'kicadSymbolki_description': 'USB to I2C/UART Protocol Converter with GPIO, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Interface_USB : MCP2221AxML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

