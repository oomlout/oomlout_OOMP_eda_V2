
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "FN406B-3-02"
    hexID = "SZKFILFN46B32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FN406-0.5-02', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'FN406B-3-02', 'kicadSymbolFootprint': 'Filter:Filter_Schaffner_FN406', 'kicadSymbolDatasheet': 'https://www.schaffner.com/products/download/product/datasheet/fn-406-ultra-compact-emc-filter/', 'kicadSymbolki_keywords': 'EMI mains', 'kicadSymbolki_description': '3A ultra compact EMI Filter, medical version', 'kicadSymbolki_fp_filters': 'Filter*Schaffner*FN406*'}])
    newPart['name'].append('FN406B-3-02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

