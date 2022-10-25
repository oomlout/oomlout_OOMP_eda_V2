
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1051T"
    hexID = "SZKINTERFACECANLINTJA151T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1051T', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/TJA1051.pdf', 'kicadSymbolki_keywords': 'High-Speed CAN Transceiver', 'kicadSymbolki_description': 'High-Speed CAN Transceiver, silent mode, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : TJA1051T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

