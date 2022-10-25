
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "SPX2920U-5.0_TO220"
    hexID = "SZKREGULATORLINEARSPX292U5TO22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM7805_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SPX2920U-5.0_TO220', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.zlgmcu.com/Sipex/LDO/PDF/spx2920.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO 5V', 'kicadSymbolki_description': '400mA Low drop-out regulator, Fixed Output 5V, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Linear : SPX2920U-5.0_TO220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

