
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS393"
    hexID = "SZK74XX74LS393"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS393', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '74xx74LS393.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL CNT CNT4', 'kicadSymbolki_description': 'Dual BCD 4-bit counter', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('74xx : 74LS393')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

