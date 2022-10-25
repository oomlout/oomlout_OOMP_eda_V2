
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM337_TO252"
    hexID = "SZKREGULATORLINEARLM337TO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM337_TO252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/1636957.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Negative', 'kicadSymbolki_description': 'Negative 1A 35V Adjustable Linear Regulator, TO-252(DPAK)', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : LM337_TO252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

