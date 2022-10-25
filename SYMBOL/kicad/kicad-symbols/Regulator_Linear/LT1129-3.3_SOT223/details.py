
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1129-3.3_SOT223"
    hexID = "SZKREGULATORLINEARLT112933SOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPX2920M3-3.3_SOT223', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1129-3.3_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/112935ff.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO fixed positive', 'kicadSymbolki_description': '700mA Micropower Low drop-out regulator, Fixed Output 3.3V, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Regulator_Linear : LT1129-3.3_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

