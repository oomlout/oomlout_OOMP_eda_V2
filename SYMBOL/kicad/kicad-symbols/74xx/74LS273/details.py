
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS273"
    hexID = "SZK74XX74LS273"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS273', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS273', 'kicadSymbolki_keywords': 'TTL DFF DFF8', 'kicadSymbolki_description': '8-bit D Flip-Flop, reset', 'kicadSymbolki_fp_filters': 'DIP?20* SO?20* SOIC?20*'}])
    newPart['name'].append('74LS273')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

