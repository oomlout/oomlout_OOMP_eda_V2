
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM3480-3.3"
    hexID = "SZKREGULATORLINEARLM34833"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3480-3.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm3480.pdf', 'kicadSymbolki_keywords': 'ldo linear fixed positive', 'kicadSymbolki_description': '100mA, Quasi Low Dropout Voltage Regulator, 3.3V positive fixed output, SOT-23 package', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : LM3480-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

