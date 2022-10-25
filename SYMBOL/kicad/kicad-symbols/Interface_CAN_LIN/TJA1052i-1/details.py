
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TJA1052i-1"
    hexID = "SZKINTERFACECANLINTJA152I1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TJA1052i-1', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/TJA1052I.pdf', 'kicadSymbolki_keywords': 'can transceiver isolated protected', 'kicadSymbolki_description': 'Isolated CAN Transceiver 1.0kV, up to 5Mbps', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : TJA1052i-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

