
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HC688"
    hexID = "SZK74XX74HC688"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS688', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HC688', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/cd54hc688.pdf', 'kicadSymbolki_keywords': 'HCMOS DECOD Arith', 'kicadSymbolki_description': '8-bit magnitude comparator', 'kicadSymbolki_fp_filters': 'DIP?20* SOIC?20* SO?20* TSSOP?20*'}])
    newPart['name'].append('74HC688')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

