
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MCP2200T-I-MQ"
    hexID = "SZKINTERFACEUMCP22TIMQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP2200-I-MQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2200T-I-MQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/200022228D.pdf', 'kicadSymbolki_keywords': 'USB UART Converter', 'kicadSymbolki_description': 'USB 2.0 to UART Protocol Converter with GPIO, TnR, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*20*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('Interface_USB : MCP2200T-I-MQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

