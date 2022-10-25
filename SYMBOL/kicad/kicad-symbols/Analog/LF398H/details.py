
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "LF398H"
    hexID = "SZKANALOGLF398H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF398H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-99-8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lf398-n.pdf', 'kicadSymbolki_keywords': 'sample hold buffer unity gain', 'kicadSymbolki_description': 'Sample And Hold Unity Gain Follower, TO-99-8', 'kicadSymbolki_fp_filters': '*TO*99*'}])
    newPart['name'].append('Analog : LF398H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

