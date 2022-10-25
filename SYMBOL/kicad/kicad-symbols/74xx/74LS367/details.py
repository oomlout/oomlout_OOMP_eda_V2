
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS367"
    hexID = "SZK74XX74LS367"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS367', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS367', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL Buffer BUS 3State', 'kicadSymbolki_description': 'Hex Bus Driver 3-state outputs', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('74xx : 74LS367')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

