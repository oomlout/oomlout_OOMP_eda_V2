
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_Dual_PMOS_S1G1S2G2D2D2D1D1"
    hexID = "SZKDEVICEQDUALPMOSS1G1S2G2D2D2D1D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_Dual_PMOS_S1G1S2G2D2D2D1D1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor PMOS P-MOS P-MOSFET', 'kicadSymbolki_description': 'Dual PMOS transistor, 8 pin package', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('Q_Dual_PMOS_S1G1S2G2D2D2D1D1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

