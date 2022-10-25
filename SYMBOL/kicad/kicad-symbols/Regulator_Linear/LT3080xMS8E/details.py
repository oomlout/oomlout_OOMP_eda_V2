
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3080xMS8E"
    hexID = "SZKREGULATORLINEARLT38XMS8E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3080xMS8E', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3080fc.pdf', 'kicadSymbolki_keywords': 'Adjustable 1.1A Low Dropout Regulator', 'kicadSymbolki_description': 'Adjustable 1.1A Single Resistor Low Dropout Regulator, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*1EP?3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LT3080xMS8E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

