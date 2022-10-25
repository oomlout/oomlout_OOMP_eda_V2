
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS573"
    hexID = "SZK74XX74LS573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS573', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '74xx/74hc573.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL DFF DFF8 LATCH 3State', 'kicadSymbolki_description': '8-bit Latch 3-state outputs', 'kicadSymbolki_fp_filters': 'DIP?20*'}])
    newPart['name'].append('74xx : 74LS573')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

