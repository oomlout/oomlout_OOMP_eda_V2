
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MCP2221AxP"
    hexID = "SZKINTERFACEUMCP2221AXP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2221AxP', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005565B.pdf', 'kicadSymbolki_keywords': 'USB I2C UART Converter Bridge', 'kicadSymbolki_description': 'USB to I2C/UART Protocol Converter with GPIO, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_USB : MCP2221AxP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

