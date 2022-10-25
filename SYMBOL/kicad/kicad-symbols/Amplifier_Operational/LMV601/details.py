
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LMV601"
    hexID = "SZKAMPLIFIEROPERATIONALLMV61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV601', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmv601.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '1MHz, Low-Power, General-Purpose, 2.7V Operational Amplifiers, SC-70-6', 'kicadSymbolki_fp_filters': '*SC*70*'}])
    newPart['name'].append('Amplifier_Operational : LMV601')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

