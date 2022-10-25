
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2574HVM-12"
    hexID = "SZKREGULATORSWITCHINGLM2574HVM12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2574HVM-12', 'kicadSymbolFootprint': 'Package_SO:SOIC-14W_7.5x9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2574.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 12V 500mA HV', 'kicadSymbolki_description': '12V, 0.5A Step-Down Voltage Regulator, High Voltage Input, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LM2574HVM-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

