
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1963AxST-1.5"
    hexID = "SZKREGULATORLINEARLT1963AXST15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1963AxST-1.5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1963aff.pdf', 'kicadSymbolki_keywords': 'LDO voltage regulator fixed', 'kicadSymbolki_description': '1.5V, 1.5A, Low Noise, Fast Transient Response LDO Regulator, SOT-223', 'kicadSymbolki_fp_filters': 'SOT*223*'}])
    newPart['name'].append('Regulator_Linear : LT1963AxST-1.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

