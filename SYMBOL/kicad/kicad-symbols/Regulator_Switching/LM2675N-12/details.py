
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2675N-12"
    hexID = "SZKREGULATORSWITCHINGLM2675N12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2674N-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2675N-12', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2675.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 12V 1A', 'kicadSymbolki_description': '12V, 1A Step-Down Voltage Regulator, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LM2675N-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

