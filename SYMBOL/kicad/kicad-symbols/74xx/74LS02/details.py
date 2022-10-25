
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS02"
    hexID = "SZK74XX74LS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS02', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74ls02', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL Nor2', 'kicadSymbolki_description': 'quad 2-input NOR gate', 'kicadSymbolki_fp_filters': 'SO14* DIP*W7.62mm*'}])
    newPart['name'].append('74xx : 74LS02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

