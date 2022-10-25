
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LTC3890-1"
    hexID = "SZKREGULATORCONTROLLERLTC3891"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3890-1', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_3.9x9.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/38901fb.pdf', 'kicadSymbolki_keywords': 'switching buck converter regulator dual-output', 'kicadSymbolki_description': '60V dual 2-phase synchronous step-down DC/DC controller, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*3.9x9.9mm*P0.635mm*'}])
    newPart['name'].append('Regulator_Controller : LTC3890-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

