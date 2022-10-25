
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP5907MFX-3.3"
    hexID = "SZKREGULATORLINEARLP597MFX33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP5907MFX-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP5907MFX-3.3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp5907.pdf', 'kicadSymbolki_keywords': 'Single Output LDO Low-Noise', 'kicadSymbolki_description': '250-mA Ultra-Low-Noise Low-IQ LDO, 3.3V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : LP5907MFX-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

