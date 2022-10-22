
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "SF14-1575F5UUC1"
    hexID = "SZKFILSF141575F5UUC1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SF14-1575F5UUA1', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'SF14-1575F5UUC1', 'kicadSymbolFootprint': 'Filter:Filter_1411-5_1.4x1.1mm', 'kicadSymbolDatasheet': 'https://global.kyocera.com/prdct/electro/product/pdf/sf14_gnss.pdf', 'kicadSymbolki_keywords': 'SAW filter', 'kicadSymbolki_description': '1575MHz SAW filter, SMD 1411', 'kicadSymbolki_fp_filters': 'Filter*1411*1.4x1.1mm*'}])
    newPart['name'].append('SF14-1575F5UUC1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

