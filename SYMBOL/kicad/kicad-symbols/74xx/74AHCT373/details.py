
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74AHCT373"
    hexID = "SZK74XX74AHCT373"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS373', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHCT373', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74ahct373.pdf', 'kicadSymbolki_keywords': 'AHCTMOS REG DFF DFF8 LATCH', 'kicadSymbolki_description': '8-bit Latch, 3-state outputs', 'kicadSymbolki_fp_filters': 'DIP?20* SOIC?20* SO?20* SSOP?20* TSSOP?20*'}])
    newPart['name'].append('74xx : 74AHCT373')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

