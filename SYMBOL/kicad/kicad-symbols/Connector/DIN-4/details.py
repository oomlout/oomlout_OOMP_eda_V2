
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DIN-4"
    hexID = "SZKCNDIN4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DIN-4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/18/40_c091_abd_e-75918.pdf', 'kicadSymbolki_keywords': 'circular DIN connector', 'kicadSymbolki_description': '4-pin DIN connector', 'kicadSymbolki_fp_filters': 'DIN*'}])
    newPart['name'].append('DIN-4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

