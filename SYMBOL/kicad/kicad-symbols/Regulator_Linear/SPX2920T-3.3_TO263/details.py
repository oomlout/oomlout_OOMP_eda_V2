
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "SPX2920T-3.3_TO263"
    hexID = "SZKREGULATORLINEARSPX292T33TO263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SPX2920T-3.3_TO263', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.zlgmcu.com/Sipex/LDO/PDF/spx2920.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO 3.3V', 'kicadSymbolki_description': '400mA Low drop-out regulator, Fixed Output 3.3V, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Linear : SPX2920T-3.3_TO263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

