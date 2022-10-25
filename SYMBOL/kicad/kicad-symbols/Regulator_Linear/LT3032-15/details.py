
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3032-15"
    hexID = "SZKREGULATORLINEARLT33215"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT3032-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3032-15', 'kicadSymbolFootprint': 'Package_DFN_QFN:Linear_DE14MA', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3032ff.pdf', 'kicadSymbolki_keywords': 'LDO low noise', 'kicadSymbolki_description': '150mA, Dual Low Dropout Linear Regulator, Positive/Negative Low Noise, 15V Output, DFN-14', 'kicadSymbolki_fp_filters': 'Linear*DE14MA*'}])
    newPart['name'].append('Regulator_Linear : LT3032-15')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

