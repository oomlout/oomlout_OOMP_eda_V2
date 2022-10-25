
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "LF398_SOIC14"
    hexID = "SZKANALOGLF398SOIC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF398_SOIC14', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lf398-n.pdf', 'kicadSymbolki_keywords': 'sample hold buffer unity gain', 'kicadSymbolki_description': 'Sample And Hold Unity Gain Follower, SOIC-14', 'kicadSymbolki_fp_filters': '*SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Analog : LF398_SOIC14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

