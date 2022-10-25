
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "MCP2022A-xxxxP"
    hexID = "SZKINTERFACECANLINMCP222AXXXXP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2022A-xxxxP', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20002298C.pdf', 'kicadSymbolki_keywords': 'LIN Transceiver regulator', 'kicadSymbolki_description': 'LIN Transceiver with Voltage Regulator, 3.3V/5V, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_CAN_LIN : MCP2022A-xxxxP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

