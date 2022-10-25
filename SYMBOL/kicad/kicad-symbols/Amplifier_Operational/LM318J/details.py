
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM318J"
    hexID = "SZKAMPLIFIEROPERATIONALLM318J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM318J', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm318-n.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Operational Amplifier, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : LM318J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

