
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2596T-5"
    hexID = "SZKREGULATORSWITCHINGLM2596T5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2596T-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2596T-5', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2596.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 5V 3A', 'kicadSymbolki_description': '5V 3A 150kHz Step-Down Voltage Regulator, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Switching : LM2596T-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

