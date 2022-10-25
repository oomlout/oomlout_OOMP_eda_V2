
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "SSM2210"
    hexID = "SZKTRANSISTORBJTSSM221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SSM2210', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/SSM2210.pdf', 'kicadSymbolki_keywords': 'audio npn dual', 'kicadSymbolki_description': 'Audio Dual Matched NPN transistor, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*8*3.9x4.9mm*P1.27mm* DIP*8*W7.62mm*'}])
    newPart['name'].append('Transistor_BJT : SSM2210')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

