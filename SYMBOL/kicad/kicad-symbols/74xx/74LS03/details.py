
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS03"
    hexID = "SZK74XX74LS3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS03', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS03', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL Nand2 OpenColl', 'kicadSymbolki_description': 'Quad 2-input NAND open collector', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm**'}])
    newPart['name'].append('74xx : 74LS03')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

