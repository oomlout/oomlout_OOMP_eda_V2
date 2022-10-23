
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1145TK"
    hexID = "SZKINTERFACECANLINTJA1145TK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1145TK', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/TJA1145.pdf', 'kicadSymbolki_keywords': 'CAN FD High Speed CAN Transceiver Sleep VIO Partial Networking SPI', 'kicadSymbolki_description': 'High-speed CAN transceiver for partial networking, DFN-14', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x4.5mm*P0.65mm*'}])
    newPart['name'].append('TJA1145TK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

