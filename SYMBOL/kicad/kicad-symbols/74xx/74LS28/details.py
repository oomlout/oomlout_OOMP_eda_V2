
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS28"
    hexID = "SZK74XX74LS28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS02', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS28', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://eeshop.unl.edu/pdf/74ls28.pdf', 'kicadSymbolki_keywords': 'TTL Nor2 Buffer', 'kicadSymbolki_description': 'quad 2-input NOR buffer NRND', 'kicadSymbolki_fp_filters': 'SO14* DIP*W7.62mm*'}])
    newPart['name'].append('74xx : 74LS28')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

