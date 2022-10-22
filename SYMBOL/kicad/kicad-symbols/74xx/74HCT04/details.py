
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HCT04"
    hexID = "SZK74XX74HCT4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS04', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HCT04', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74HC_HCT04.pdf', 'kicadSymbolki_keywords': 'HCTMOS not inv', 'kicadSymbolki_description': 'Hex Inverter', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SSOP?14* TSSOP?14*'}])
    newPart['name'].append('74HCT04')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

