
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LTC2851xDD"
    hexID = "SZKINTERFACEUARTLTC2851XDD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2851xDD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.5mm_EP1.66x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/285012fe.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver full duplex', 'kicadSymbolki_description': 'RS-485, RS-422 Full duplex 20Mbps transceiver, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface_UART : LTC2851xDD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

