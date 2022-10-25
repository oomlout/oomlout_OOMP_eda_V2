
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2672M-3.3"
    hexID = "SZKREGULATORSWITCHINGLM2672M33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2672M-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2672M-3.3', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2672.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 3.3V 1A', 'kicadSymbolki_description': '3.3V, 1A Step-Down Voltage Regulator, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LM2672M-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

