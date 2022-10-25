
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HC02"
    hexID = "SZK74XX74HC2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS02', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HC02', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74hc02', 'kicadSymbolki_keywords': 'HCMOS Nor2', 'kicadSymbolki_description': 'quad 2-input NOR gate', 'kicadSymbolki_fp_filters': 'SO14* DIP*W7.62mm*'}])
    newPart['name'].append('74xx : 74HC02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

