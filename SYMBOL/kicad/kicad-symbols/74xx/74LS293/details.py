
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS293"
    hexID = "SZK74XX74LS293"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS290', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS293', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS293', 'kicadSymbolki_keywords': 'TTL CNT CNT4', 'kicadSymbolki_description': '4-bit binary counter', 'kicadSymbolki_fp_filters': 'DIP?12*'}])
    newPart['name'].append('74xx : 74LS293')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

