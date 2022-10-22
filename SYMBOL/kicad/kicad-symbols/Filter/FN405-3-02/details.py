
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "FN405-3-02"
    hexID = "SZKFILFN4532"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FN405-0.5-02', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'FN405-3-02', 'kicadSymbolFootprint': 'Filter:Filter_Schaffner_FN405', 'kicadSymbolDatasheet': 'https://www.schaffner.com/de/produkte/download/product/datasheet/fn-405-pcb-mounting-filter/', 'kicadSymbolki_keywords': 'EMI', 'kicadSymbolki_description': '3A, 250VAC, 50/60Hz line filter', 'kicadSymbolki_fp_filters': 'Filter*Schaffner*FN405*'}])
    newPart['name'].append('FN405-3-02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

