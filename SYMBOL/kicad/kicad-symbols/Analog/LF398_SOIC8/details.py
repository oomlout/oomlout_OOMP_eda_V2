
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "LF398_SOIC8"
    hexID = "SZKANALOGLF398SOIC8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LF398_DIP8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF398_SOIC8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/lt0398s8.pdf', 'kicadSymbolki_keywords': 'sample hold buffer unity gain', 'kicadSymbolki_description': 'Sample And Hold Unity Gain Follower, SOIC-8', 'kicadSymbolki_fp_filters': '*SOIC*3.9x4.9mm*P1.27mm* *DIP*W7.62mm*'}])
    newPart['name'].append('Analog : LF398_SOIC8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

