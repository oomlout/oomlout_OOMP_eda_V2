
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS241_Split"
    hexID = "SZK74XX74LS241SPLIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS241_Split', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74ls241.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': '7400 logic ttl low power schottky', 'kicadSymbolki_description': 'Octal Buffer and Line Driver With 3-State Output, complementary enables, non-inverting outputs, split symbol', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x12.8mm*P1.27mm* *SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('74LS241_Split')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

