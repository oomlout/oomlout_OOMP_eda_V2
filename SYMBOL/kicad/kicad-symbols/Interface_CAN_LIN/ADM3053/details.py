
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "ADM3053"
    hexID = "SZKINTERFACECANLINADM353"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM3053', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADM3053.pdf', 'kicadSymbolki_keywords': 'can transceiver isolated protected', 'kicadSymbolki_description': 'Isolated CAN Transceiver, integrated isolated DC-DC converter, 1Mbps', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : ADM3053')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

