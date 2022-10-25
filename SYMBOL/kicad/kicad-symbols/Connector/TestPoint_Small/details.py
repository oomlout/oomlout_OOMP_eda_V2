
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "TestPoint_Small"
    hexID = "SZKCNTPSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TP', 'kicadSymbolValue': 'TestPoint_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'test point tp', 'kicadSymbolki_description': 'test point', 'kicadSymbolki_fp_filters': 'Pin* Test*'}])
    newPart['name'].append('Connector : TestPoint_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

