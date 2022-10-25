
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2050-500-EP"
    hexID = "SZKINTERFACECANLINMCP255EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP2050-330-EP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2050-500-EP', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22299B.pdf', 'kicadSymbolki_keywords': 'LIN transceiver regulator', 'kicadSymbolki_description': 'LIN Transceiver with Voltage Regulator, 5V, PDIP', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2050-500-EP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

