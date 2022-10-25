
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "7400"
    hexID = "SZK74XX74"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS00', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '7400', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn7400', 'kicadSymbolki_keywords': 'TTL nand 2-input', 'kicadSymbolki_description': 'quad 2-input NAND gate', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SO14*'}])
    newPart['name'].append('74xx : 7400')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

