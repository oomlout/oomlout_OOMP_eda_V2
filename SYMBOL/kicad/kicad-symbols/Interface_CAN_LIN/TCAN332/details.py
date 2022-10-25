
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "TCAN332"
    hexID = "SZKINTERFACECANLINTCAN332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCAN332', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tcan337.pdf', 'kicadSymbolki_keywords': 'High-Speed CAN Transceiver', 'kicadSymbolki_description': 'High-Speed CAN Transceiver, 1Mbps, 3.3V supply, SOT-23-8/SOIC-8', 'kicadSymbolki_fp_filters': '*TSOT?23* *SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : TCAN332')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

