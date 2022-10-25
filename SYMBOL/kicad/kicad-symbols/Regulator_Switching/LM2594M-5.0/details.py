
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2594M-5.0"
    hexID = "SZKREGULATORSWITCHINGLM2594M5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2594M-3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2594M-5.0', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2594.pdf', 'kicadSymbolki_keywords': 'buck converter regulator step-down voltage simple switcher fixed', 'kicadSymbolki_description': '5.0V, 0.5A SIMPLE SWITCHER® Step-Down Voltage Regulator, Maximum VIN 45V, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*'}])
    newPart['name'].append('Regulator_Switching : LM2594M-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

