
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3011xDD"
    hexID = "SZKREGULATORLINEARLT311XDD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3011xDD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.65x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3011f.pdf', 'kicadSymbolki_keywords': 'variable regulator', 'kicadSymbolki_description': '50mA, 3V to 80V Low Dropout Micropower Linear Regulator with PWRGD, DFN-10', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Linear : LT3011xDD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

