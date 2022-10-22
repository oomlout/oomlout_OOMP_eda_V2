
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "SAFFB1G58KA0F0A"
    hexID = "SZKFILSAFFB1G58KAFA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B39162B8813P810', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'SAFFB1G58KA0F0A', 'kicadSymbolFootprint': 'Filter:Filter_1109-5_1.1x0.9mm', 'kicadSymbolDatasheet': 'https://www.murata.com/~/media/webrenewal/support/library/catalog/products/filter/rf/p73e.ashx?la=en', 'kicadSymbolki_keywords': 'SAW filter', 'kicadSymbolki_description': 'Murata 1575.42/1602MHz SAW filter, SMD 1109', 'kicadSymbolki_fp_filters': 'Filter*1109*1.1x0.9mm*'}])
    newPart['name'].append('SAFFB1G58KA0F0A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

