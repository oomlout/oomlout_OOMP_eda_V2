
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "HDMI_B"
    hexID = "SZKCNHDMIB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HDMI_B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pinouts.ru/Video/hdmi_pinout.shtml', 'kicadSymbolki_keywords': 'hdmi conn', 'kicadSymbolki_description': 'HDMI type B connector', 'kicadSymbolki_fp_filters': 'HDMI*B*'}])
    newPart['name'].append('Connector : HDMI_B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

