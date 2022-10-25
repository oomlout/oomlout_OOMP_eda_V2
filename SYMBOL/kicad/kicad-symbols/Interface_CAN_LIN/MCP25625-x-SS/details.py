
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP25625-x-SS"
    hexID = "SZKINTERFACECANLINMCP25625XSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP25625-x-SS', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005282B.pdf', 'kicadSymbolki_keywords': 'CAN Controller SPI Transceiver', 'kicadSymbolki_description': 'Stand-Alone CAN Controller with SPI Interface and integated Transceiver, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP25625-x-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

