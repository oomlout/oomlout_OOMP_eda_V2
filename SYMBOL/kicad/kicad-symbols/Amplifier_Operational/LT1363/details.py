
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LT1363"
    hexID = "SZKAMPLIFIEROPERATIONALLT1363"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OP07', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1363', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1363fa.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '70MHz, 1000V/µs Operational Amplifier, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TO*99*'}])
    newPart['name'].append('Amplifier_Operational : LT1363')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

