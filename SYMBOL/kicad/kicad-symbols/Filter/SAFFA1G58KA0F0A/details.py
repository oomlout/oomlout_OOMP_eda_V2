
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "SAFFA1G58KA0F0A"
    hexID = "SZKFILSAFFA1G58KAFA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SF14-1575F5UUA1', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'SAFFA1G58KA0F0A', 'kicadSymbolFootprint': 'Filter:Filter_1411-5_1.4x1.1mm', 'kicadSymbolDatasheet': 'https://www.murata.com/~/media/webrenewal/support/library/catalog/products/filter/rf/p73e.ashx?la=en', 'kicadSymbolki_keywords': 'SAW filter', 'kicadSymbolki_description': 'Murata 1575.42/1602MHz SAW filter, SMD 1411', 'kicadSymbolki_fp_filters': 'Filter*1411*1.4x1.1mm*'}])
    newPart['name'].append('SAFFA1G58KA0F0A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

