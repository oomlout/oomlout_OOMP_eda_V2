
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS174"
    hexID = "SZK74XX74LS174"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS174', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS174', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL REG REG6 DFF', 'kicadSymbolki_description': 'Hex D-type Flip-Flop, reset', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('74xx : 74LS174')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

