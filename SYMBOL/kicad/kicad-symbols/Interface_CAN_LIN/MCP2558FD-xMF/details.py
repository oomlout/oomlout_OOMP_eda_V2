
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2558FD-xMF"
    hexID = "SZKINTERFACECANLINMCP2558FDXMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2558FD-xMF', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/20005533A.pdf', 'kicadSymbolki_keywords': 'CAN FD Transceiver', 'kicadSymbolki_description': 'CAN FD Transceiver with Silent Mode, up to 8 Mbps, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2558FD-xMF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

