
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2515-xSO"
    hexID = "SZKINTERFACECANLINMCP2515XSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2515-xSO', 'kicadSymbolFootprint': 'Package_SO:SOIC-18W_7.5x11.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21801e.pdf', 'kicadSymbolki_keywords': 'CAN Controller SPI', 'kicadSymbolki_description': 'Stand-Alone CAN Controller with SPI Interface, SOIC-18', 'kicadSymbolki_fp_filters': 'SOIC*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2515-xSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

