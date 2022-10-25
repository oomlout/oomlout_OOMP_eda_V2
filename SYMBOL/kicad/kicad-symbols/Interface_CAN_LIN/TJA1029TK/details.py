
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1029TK"
    hexID = "SZKINTERFACECANLINTJA129TK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1029TK', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/TJA1029.pdf', 'kicadSymbolki_keywords': 'LIN 2.2A/SAE J2602 Transceiver HVSON-8', 'kicadSymbolki_description': 'LIN 2.2A/SAE J2602 transceiver with TXD dominant timeout, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Interface_CAN_LIN : TJA1029TK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

