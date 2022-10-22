
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "1FP45-0R"
    hexID = "SZKFIL1FP45R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': '1FP45-0R', 'kicadSymbolFootprint': 'Filter:Filter_FILTERCON_1FPxx', 'kicadSymbolDatasheet': 'https://filtercon.com.pl/wp-content/uploads/2019/07/Karta-katalogowa-FP-12-1.pdf', 'kicadSymbolki_keywords': 'EMI', 'kicadSymbolki_description': '0.5A, 250VAC, 50/60Hz line filter', 'kicadSymbolki_fp_filters': 'Filter*FILTERCON*1FPxx*'}])
    newPart['name'].append('1FP45-0R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

