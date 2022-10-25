
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MCP2200-I-SO"
    hexID = "SZKINTERFACEUMCP22ISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2200-I-SO', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/200022228D.pdf', 'kicadSymbolki_keywords': 'USB UART Converter', 'kicadSymbolki_description': 'USB 2.0 to UART Protocol Converter with GPIO, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*20*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('Interface_USB : MCP2200-I-SO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

