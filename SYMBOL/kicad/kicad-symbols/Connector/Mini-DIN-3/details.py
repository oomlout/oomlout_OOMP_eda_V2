
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Mini-DIN-3"
    hexID = "SZKCNMDIN3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Mini-DIN-3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.assmann-wsw.com/fileadmin/catalogue/10_MiniDIN_rev4-0.pdf', 'kicadSymbolki_keywords': 'Mini-DIN', 'kicadSymbolki_description': '3-pin Mini-DIN connector', 'kicadSymbolki_fp_filters': 'MINI?DIN*'}])
    newPart['name'].append('Mini-DIN-3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

