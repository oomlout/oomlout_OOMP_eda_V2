
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NVC8674DS120"
    hexID = "SZKREGULATORLINEARNVC8674DS12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NVC8674DS50', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NVC8674DS120', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCV8674-D.PDF', 'kicadSymbolki_keywords': 'ldo regulator 12V', 'kicadSymbolki_description': '350mA, 12.0V Very Low Iq Low Dropout Linear Regulator, TO-263-2', 'kicadSymbolki_fp_filters': 'TO*263*'}])
    newPart['name'].append('Regulator_Linear : NVC8674DS120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

