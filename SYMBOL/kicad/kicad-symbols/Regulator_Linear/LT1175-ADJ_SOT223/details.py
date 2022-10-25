
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1175-ADJ_SOT223"
    hexID = "SZKREGULATORLINEARLT1175ADJSOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1175-5_SOT223', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1175-ADJ_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1175ff.pdf', 'kicadSymbolki_keywords': 'linear regulator LDO negative adjustable', 'kicadSymbolki_description': '500mA Negative Low Dropout Micropower Regulator, adjustable output voltage, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Regulator_Linear : LT1175-ADJ_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

