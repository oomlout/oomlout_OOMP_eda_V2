
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM117_TO3"
    hexID = "SZKREGULATORLINEARLM117TO3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM317_TO3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM117_TO3', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm317.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1,5A Positive', 'kicadSymbolki_description': '1,5A 35V Adjustable Linear Regulator, TO-3', 'kicadSymbolki_fp_filters': 'TO?3*'}])
    newPart['name'].append('Regulator_Linear : LM117_TO3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

