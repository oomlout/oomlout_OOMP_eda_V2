
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMH7324"
    hexID = "SZKCOMPARATORLMH7324"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMH7324', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmh7324.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp push-pull complementary', 'kicadSymbolki_description': 'Quad 700 ps High Speed Comparator with RSPECL Outputs, WQFN-32', 'kicadSymbolki_fp_filters': 'WQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('LMH7324')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

