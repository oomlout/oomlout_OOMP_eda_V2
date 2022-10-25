
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "LF398_DIP8"
    hexID = "SZKANALOGLF398DIP8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF398_DIP8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lf398-n.pdf', 'kicadSymbolki_keywords': 'sample hold buffer unity gain', 'kicadSymbolki_description': 'Sample And Hold Unity Gain Follower, DIP-8', 'kicadSymbolki_fp_filters': '*SOIC*3.9x4.9mm*P1.27mm* *DIP*W7.62mm*'}])
    newPart['name'].append('Analog : LF398_DIP8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

