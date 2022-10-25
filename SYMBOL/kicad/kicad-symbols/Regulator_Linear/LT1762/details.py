
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1762"
    hexID = "SZKREGULATORLINEARLT1762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1962', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1762', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LT1762.pdf', 'kicadSymbolki_keywords': 'LDO ADJ', 'kicadSymbolki_description': '150mA, Adjustable, Low Noise, Micropower LDO Regulator, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LT1762')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

