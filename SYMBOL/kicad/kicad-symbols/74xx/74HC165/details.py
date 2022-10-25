
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HC165"
    hexID = "SZK74XX74HC165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS165', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HC165', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74HC_HCT165.pdf', 'kicadSymbolki_keywords': '8 bit shift register parallel load cmos', 'kicadSymbolki_description': 'Shift Register, 8-bit, Parallel Load', 'kicadSymbolki_fp_filters': 'DIP?16* SO*16*3.9x9.9mm*P1.27mm* SSOP*16*5.3x6.2mm*P0.65mm* TSSOP*16*4.4x5mm*P0.65*'}])
    newPart['name'].append('74xx : 74HC165')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

