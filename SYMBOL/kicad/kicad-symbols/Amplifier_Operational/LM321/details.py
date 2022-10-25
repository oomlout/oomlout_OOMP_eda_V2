
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM321"
    hexID = "SZKAMPLIFIEROPERATIONALLM321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM321', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm321.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Low Power Single Operational Amplifier, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : LM321')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

