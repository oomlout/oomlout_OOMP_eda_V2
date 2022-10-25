
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM2937xS"
    hexID = "SZKREGULATORLINEARLM2937XS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPX2920T-3.3_TO263', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2937xS', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2937.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator Low Dropuout Positive LDO', 'kicadSymbolki_description': '500-mA Low Dropout Regulator, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Linear : LM2937xS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

