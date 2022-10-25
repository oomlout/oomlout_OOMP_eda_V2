
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS241"
    hexID = "SZK74XX74LS241"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS241', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74ls241.pdf', 'kicadSymbolki_keywords': '7400 logic ttl low power schottky', 'kicadSymbolki_description': 'Octal Buffer and Line Driver With 3-State Output, complementary enables, non-inverting outputs', 'kicadSymbolki_fp_filters': 'DIP?20*'}])
    newPart['name'].append('74xx : 74LS241')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

