
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS243"
    hexID = "SZK74XX74LS243"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS243', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS243', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'TTL Buffer 3State BUS BIDI', 'kicadSymbolki_description': '4-bit Bus Transceiver', 'kicadSymbolki_fp_filters': 'DIP?12*'}])
    newPart['name'].append('74xx : 74LS243')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

