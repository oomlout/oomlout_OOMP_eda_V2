
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "MCP23017_SP"
    hexID = "SZKINTERFACEEXPANSIONMCP2317SP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP23017_SP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf', 'kicadSymbolki_keywords': 'I2C parallel port expander', 'kicadSymbolki_description': '16-bit I/O expander, I2C, interrupts, w pull-ups, SPDIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_Expansion : MCP23017_SP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

