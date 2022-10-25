
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "HDMI_A"
    hexID = "SZKCNHDMIA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HDMI_A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://en.wikipedia.org/wiki/HDMI', 'kicadSymbolki_keywords': 'hdmi conn', 'kicadSymbolki_description': 'HDMI type A connector', 'kicadSymbolki_fp_filters': 'HDMI*A*'}])
    newPart['name'].append('Connector : HDMI_A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

