
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM318H"
    hexID = "SZKAMPLIFIEROPERATIONALLM318H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM318M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM318H', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm318-n.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Operational Amplifier, TO-99-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TO*99*'}])
    newPart['name'].append('Amplifier_Operational : LM318H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

