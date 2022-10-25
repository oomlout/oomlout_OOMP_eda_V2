
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3080xST"
    hexID = "SZKREGULATORLINEARLT38XST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3080xST', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3080fc.pdf', 'kicadSymbolki_keywords': 'Adjustable 1.1A Low Dropout Regulator', 'kicadSymbolki_description': 'Adjustable 1.1A Single Resistor Low Dropout Regulator, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Regulator_Linear : LT3080xST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

