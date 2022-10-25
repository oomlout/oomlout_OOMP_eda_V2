
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1086-12"
    hexID = "SZKREGULATORLINEARLT18612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1084-3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1086-12', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1086ffs.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator Fixed 1.5A Positive LDO', 'kicadSymbolki_description': '1.5A 25V LDO Linear Regulator, Fixed Output 12V, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LT1086-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

