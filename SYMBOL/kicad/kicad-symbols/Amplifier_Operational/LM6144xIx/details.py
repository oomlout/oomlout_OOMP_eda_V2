
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM6144xIx"
    hexID = "SZKAMPLIFIEROPERATIONALLM6144XIX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM6144xIx', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm6142.pdf', 'kicadSymbolki_keywords': 'quad opamp rail', 'kicadSymbolki_description': 'Low-Power, Quad-Operational Amplifiers, 17MHz, DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : LM6144xIx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

