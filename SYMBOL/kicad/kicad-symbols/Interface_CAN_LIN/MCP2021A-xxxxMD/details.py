
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2021A-xxxxMD"
    hexID = "SZKINTERFACECANLINMCP221AXXXXMD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2021A-xxxxMD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20002298C.pdf', 'kicadSymbolki_keywords': 'LIN Transceiver regulator', 'kicadSymbolki_description': 'LIN Transceiver with Voltage Regulator, 3.3V/5V, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*4x4mm*P0.8mm*EP2.5x3.6mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2021A-xxxxMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

