
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2517FD-xJHA"
    hexID = "SZKINTERFACECANLINMCP2517FDXJHA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2517FD-xJHA', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/20005688A.pdf', 'kicadSymbolki_keywords': 'CAN FD Controller SPI', 'kicadSymbolki_description': 'External CAN FD Controller with SPI Interface, VDFN-14', 'kicadSymbolki_fp_filters': 'DFN*3x4.5mm*P0.65mm*EP1.65x4.25mm*'}])
    newPart['name'].append('MCP2517FD-xJHA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

