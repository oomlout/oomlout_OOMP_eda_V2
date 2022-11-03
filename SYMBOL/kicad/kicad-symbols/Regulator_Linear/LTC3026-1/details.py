
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LTC3026-1"
    hexID = "SZKREGULATORLINEARLTC3261"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3026-1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/30261f.pdf', 'kicadSymbolki_keywords': 'regulator LDO positive adjustable', 'kicadSymbolki_description': '1.14V-5.5V, 1.5A Low Input Voltage VLDO Linear Regulator', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*EP1.65x2.38mm* MSOP*1EP*3x3mm*P0.5mm*EP1.68x1.88mm*'}])
    newPart['name'].append('Regulator_Linear : LTC3026-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

