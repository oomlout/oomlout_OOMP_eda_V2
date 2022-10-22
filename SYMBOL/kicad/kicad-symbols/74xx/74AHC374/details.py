
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74AHC374"
    hexID = "SZK74XX74AHC374"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS374', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHC374', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74AHC_AHCT374.pdf', 'kicadSymbolki_keywords': 'AHCMOS DFF DFF8 REG 3State', 'kicadSymbolki_description': '8-bit Register, 3-state outputs', 'kicadSymbolki_fp_filters': 'DIP?20* SOIC?20* SO?20*'}])
    newPart['name'].append('74AHC374')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

