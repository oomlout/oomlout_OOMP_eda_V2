
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "SPX2920M3-5.0_SOT223"
    hexID = "SZKREGULATORLINEARSPX292M35SOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPX2920M3-3.3_SOT223', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SPX2920M3-5.0_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.zlgmcu.com/Sipex/LDO/PDF/spx2920.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO 5V', 'kicadSymbolki_description': '400mA Low drop-out regulator, Fixed Output 5V, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Regulator_Linear : SPX2920M3-5.0_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

