
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM79M12_TO220"
    hexID = "SZKREGULATORLINEARLM79M12TO22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM7905_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM79M12_TO220', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC79M00-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 500mA Negative', 'kicadSymbolki_description': 'Negative 500mA 35V Linear Regulator, Fixed Output 12V, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Linear : LM79M12_TO220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

