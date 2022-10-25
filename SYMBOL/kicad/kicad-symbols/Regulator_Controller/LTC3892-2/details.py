
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LTC3892-2"
    hexID = "SZKREGULATORCONTROLLERLTC38922"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC3892', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3892-2', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/38921fc.pdf', 'kicadSymbolki_keywords': 'switching buck converter regulator dual-output', 'kicadSymbolki_description': '60V dual 2-phase synchronous step-down DC/DC controller, pulse-skipping, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Controller : LTC3892-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

