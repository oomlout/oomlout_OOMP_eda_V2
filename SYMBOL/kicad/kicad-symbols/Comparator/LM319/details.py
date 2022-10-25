
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LM319"
    hexID = "SZKCOMPARATORLM319"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM319', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm319-n.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp open collector', 'kicadSymbolki_description': 'High Speed Dual Comparator, DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Comparator : LM319')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

