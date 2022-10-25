
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1964-BYP"
    hexID = "SZKREGULATORLINEARLT1964BYP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1964-BYP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1964fb.pdf', 'kicadSymbolki_keywords': 'REGULATOR POSITIVE POWER LDO adjustable', 'kicadSymbolki_description': 'MICROPOWER 200mA Low Noise LDO negative regulator, adjustable output, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : LT1964-BYP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

