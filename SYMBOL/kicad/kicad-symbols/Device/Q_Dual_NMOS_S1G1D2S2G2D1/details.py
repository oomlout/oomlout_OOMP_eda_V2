
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_Dual_NMOS_S1G1D2S2G2D1"
    hexID = "SZKDEVICEQDUALNMOSS1G1D2S2G2D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_Dual_NMOS_S1G1D2S2G2D1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor NMOS N-MOS N-MOSFET', 'kicadSymbolki_description': 'Dual NMOS transistor, 6 pin package', 'kicadSymbolki_fp_filters': 'TSOP* SC?70* SC?88* SOT?363*'}])
    newPart['name'].append('Device : Q_Dual_NMOS_S1G1D2S2G2D1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

