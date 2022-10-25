
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2672N-5.0"
    hexID = "SZKREGULATORSWITCHINGLM2672N5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2672N-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2672N-5.0', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2672.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 5V 1A', 'kicadSymbolki_description': '5V, 1A Step-Down Voltage Regulator, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LM2672N-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

