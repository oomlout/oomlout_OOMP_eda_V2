
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS90"
    hexID = "SZK74XX74LS9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS90', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS90', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL CNT CNT4', 'kicadSymbolki_description': 'BCD Counter ( div 2 & div 5 )', 'kicadSymbolki_fp_filters': 'DIP?12*'}])
    newPart['name'].append('74xx : 74LS90')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

