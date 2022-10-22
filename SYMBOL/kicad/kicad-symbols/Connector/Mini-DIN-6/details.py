
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Mini-DIN-6"
    hexID = "SZKCNMDIN6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Mini-DIN-6', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://service.powerdynamics.com/ec/Catalog17/Section%2011.pdf', 'kicadSymbolki_keywords': 'Mini-DIN', 'kicadSymbolki_description': '6-pin Mini-DIN connector', 'kicadSymbolki_fp_filters': 'MINI?DIN*'}])
    newPart['name'].append('Mini-DIN-6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

