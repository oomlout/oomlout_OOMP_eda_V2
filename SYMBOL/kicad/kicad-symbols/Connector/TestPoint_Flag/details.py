
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "TestPoint_Flag"
    hexID = "SZKCNTPFLAG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TP', 'kicadSymbolValue': 'TestPoint_Flag', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'test point tp', 'kicadSymbolki_description': 'test point (alternative flag-style design)', 'kicadSymbolki_fp_filters': 'Pin* Test*'}])
    newPart['name'].append('Connector : TestPoint_Flag')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

