
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DIN-5"
    hexID = "SZKCNDIN5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DIN-5', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/18/40_c091_abd_e-75918.pdf', 'kicadSymbolki_keywords': 'circular DIN connector', 'kicadSymbolki_description': '5-pin DIN connector', 'kicadSymbolki_fp_filters': 'DIN*'}])
    newPart['name'].append('DIN-5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

