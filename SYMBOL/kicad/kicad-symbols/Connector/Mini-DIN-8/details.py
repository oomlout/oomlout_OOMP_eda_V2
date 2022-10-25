
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Mini-DIN-8"
    hexID = "SZKCNMDIN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Mini-DIN-8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://service.powerdynamics.com/ec/Catalog17/Section%2011.pdf', 'kicadSymbolki_keywords': 'Mini-DIN', 'kicadSymbolki_description': '8-pin Mini-DIN connector', 'kicadSymbolki_fp_filters': 'MINI?DIN*'}])
    newPart['name'].append('Connector : Mini-DIN-8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

