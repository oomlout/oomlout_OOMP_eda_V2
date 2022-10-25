
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM337_TO39"
    hexID = "SZKREGULATORLINEARLM337TO39"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM337_TO39', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm337-n.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 500mA Negative', 'kicadSymbolki_description': 'Negative 500mA 35V Adjustable Linear Regulator, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('Regulator_Linear : LM337_TO39')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

