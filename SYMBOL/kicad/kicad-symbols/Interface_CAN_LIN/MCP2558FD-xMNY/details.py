
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2558FD-xMNY"
    hexID = "SZKINTERFACECANLINMCP2558FDXMNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2558FD-xMNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/20005533A.pdf', 'kicadSymbolki_keywords': 'CAN FD Transceiver', 'kicadSymbolki_description': 'CAN FD Transceiver with Silent Mode, up to 8 Mbps, TDFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2558FD-xMNY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

