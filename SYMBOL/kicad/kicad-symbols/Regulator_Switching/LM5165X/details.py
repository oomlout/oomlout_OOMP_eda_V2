
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5165X"
    hexID = "SZKREGULATORSWITCHINGLM5165X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5165X', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5165.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator fixed 5V', 'kicadSymbolki_description': '150mA Synchronous Buck Converter With Ultra-Low IQ, 3V-65V input, 5.0V fixed output voltage, DFN-10', 'kicadSymbolki_fp_filters': 'Texas*PVSON*N10*'}])
    newPart['name'].append('Regulator_Switching : LM5165X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

