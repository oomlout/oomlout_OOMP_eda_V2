
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1086-ADJ"
    hexID = "SZKREGULATORLINEARLT186ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1084-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1086-ADJ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1086ffs.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator Adjustable 1.5A Positive LDO', 'kicadSymbolki_description': '1.5A 25V LDO Linear Regulator, Adjustable Output, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LT1086-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

