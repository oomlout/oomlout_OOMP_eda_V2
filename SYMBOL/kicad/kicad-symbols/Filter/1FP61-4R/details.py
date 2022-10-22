
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "1FP61-4R"
    hexID = "SZKFIL1FP614R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1FP45-0R', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': '1FP61-4R', 'kicadSymbolFootprint': 'Filter:Filter_FILTERCON_1FPxx', 'kicadSymbolDatasheet': 'https://filtercon.com.pl/wp-content/uploads/2019/07/Karta-katalogowa-FP-12-1.pdf', 'kicadSymbolki_keywords': 'EMI', 'kicadSymbolki_description': '4A, 250VAC, 50/60Hz line filter', 'kicadSymbolki_fp_filters': 'Filter*FILTERCON*1FPxx*'}])
    newPart['name'].append('1FP61-4R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

