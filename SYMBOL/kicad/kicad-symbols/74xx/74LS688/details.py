
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS688"
    hexID = "SZK74XX74LS688"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS688', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS688', 'kicadSymbolki_keywords': 'TTL DECOD Arith', 'kicadSymbolki_description': '8-bit magnitude comparator', 'kicadSymbolki_fp_filters': 'DIP?20* SOIC?20* SO?20* TSSOP?20*'}])
    newPart['name'].append('74xx : 74LS688')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

