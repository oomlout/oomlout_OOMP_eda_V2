
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP1108AN"
    hexID = "SZKREGULATORSWITCHINGADP118AN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1073CN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP1108AN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP1108.pdf', 'kicadSymbolki_keywords': 'switching buck boost converter step-down step-up', 'kicadSymbolki_description': 'Micropower DC-DC converter, step-up or step-down operation, 2V-30Vin, adjustable output voltage, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : ADP1108AN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

