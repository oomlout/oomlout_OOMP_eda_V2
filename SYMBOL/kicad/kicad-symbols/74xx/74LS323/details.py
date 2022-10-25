
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS323"
    hexID = "SZK74XX74LS323"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS323', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS323', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL REG SR SR8', 'kicadSymbolki_description': '8-bit Universal Shift/Storage Register', 'kicadSymbolki_fp_filters': 'DIP?20*'}])
    newPart['name'].append('74xx : 74LS323')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

