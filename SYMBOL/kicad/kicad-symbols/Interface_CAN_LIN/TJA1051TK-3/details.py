
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1051TK-3"
    hexID = "SZKINTERFACECANLINTJA151TK3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1051TK-3', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/TJA1051.pdf', 'kicadSymbolki_keywords': 'High-Speed CAN Transceiver HVSON-8', 'kicadSymbolki_description': 'High-Speed CAN Transceiver, separate VIO, silent mode, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('TJA1051TK-3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

