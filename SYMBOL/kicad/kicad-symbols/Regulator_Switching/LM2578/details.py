
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2578"
    hexID = "SZKREGULATORSWITCHINGLM2578"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM3578', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2578', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm3578a.pdf', 'kicadSymbolki_keywords': 'switching regulator', 'kicadSymbolki_description': '750mA, Switching Regulator, adjustable output voltage, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*'}])
    newPart['name'].append('Regulator_Switching : LM2578')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

