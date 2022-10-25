
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM337_TO263"
    hexID = "SZKREGULATORLINEARLM337TO263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM337_TO263', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/LM337-D.PDF', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Negative', 'kicadSymbolki_description': 'Negative 1A 35V Adjustable Linear Regulator, TO-263(D2-PAK)', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Linear : LM337_TO263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

