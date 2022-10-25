
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5166Y"
    hexID = "SZKREGULATORSWITCHINGLM5166Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5165X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5166Y', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5166.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator fixed 3V3', 'kicadSymbolki_description': '500mA Synchronous Buck Converter With Ultra-Low IQ, 3V-65V input, 3.3V fixed output voltage, DFN-10', 'kicadSymbolki_fp_filters': 'Texas*PVSON*N10*'}])
    newPart['name'].append('Regulator_Switching : LM5166Y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

