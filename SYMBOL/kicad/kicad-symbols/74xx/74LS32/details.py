
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS32"
    hexID = "SZK74XX74LS32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS32', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS32', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL Or2', 'kicadSymbolki_description': 'Quad 2-input OR', 'kicadSymbolki_fp_filters': 'DIP?14*'}])
    newPart['name'].append('74xx : 74LS32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

