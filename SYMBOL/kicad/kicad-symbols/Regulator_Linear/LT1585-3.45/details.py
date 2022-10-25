
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1585-3.45"
    hexID = "SZKREGULATORLINEARLT1585345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1585-3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1585-3.45', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/158457a.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 4.6A Positive Fixed', 'kicadSymbolki_description': 'Positive 4.6A 35V Low Dropout Fast Response Linear Regulator, Fixed Output 3.45V, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LT1585-3.45')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

