
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LTC2858xDD-2"
    hexID = "SZKINTERFACEUARTLTC2858XDD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC2852xDD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2858xDD-2', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.65x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/285678fg.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver full duplex', 'kicadSymbolki_description': 'RS-485, RS-422 Full duplex 250kbps transceiver, DFN-10', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface_UART : LTC2858xDD-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

