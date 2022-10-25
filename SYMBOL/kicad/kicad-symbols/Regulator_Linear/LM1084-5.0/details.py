
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM1084-5.0"
    hexID = "SZKREGULATORLINEARLM1845"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1084-3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM1084-5.0', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm1084.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 5A Positive', 'kicadSymbolki_description': '5A 27V Linear Regulator, Fixed Output 5.0V, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LM1084-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

