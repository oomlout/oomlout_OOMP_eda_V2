
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1042TK-3"
    hexID = "SZKINTERFACECANLINTJA142TK3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TJA1049TK-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1042TK-3', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/TJA1042.pdf', 'kicadSymbolki_keywords': 'High-Speed CAN Transceiver HVSON-8', 'kicadSymbolki_description': 'High-Speed CAN Transceiver, separate VIO, standby mode, DFN-8-1EP', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.65mm* HVSON*'}])
    newPart['name'].append('Interface_CAN_LIN : TJA1042TK-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

