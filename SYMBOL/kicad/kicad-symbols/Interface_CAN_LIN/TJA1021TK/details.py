
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1021TK"
    hexID = "SZKINTERFACECANLINTJA121TK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1021TK', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/TJA1021.pdf', 'kicadSymbolki_keywords': 'LIN 2.1 SAE J2602 Transceiver HVSON-8', 'kicadSymbolki_description': 'LIN 2.1/SAE J2602 transceiver, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('TJA1021TK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

