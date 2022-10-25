
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM341T-05_TO220"
    hexID = "SZKREGULATORLINEARLM341T5TO22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM7805_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM341T-05_TO220', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm341.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 500mA Positive', 'kicadSymbolki_description': 'Positive 500mA 35V Linear Regulator, Fixed Output 5V, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Linear : LM341T-05_TO220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

