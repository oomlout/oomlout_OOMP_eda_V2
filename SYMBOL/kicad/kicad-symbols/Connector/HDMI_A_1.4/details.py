
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "HDMI_A_1.4"
    hexID = "SZKCNHDMIA14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HDMI_A_1.4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://en.wikipedia.org/wiki/HDMI', 'kicadSymbolki_keywords': 'hdmi conn', 'kicadSymbolki_description': 'HDMI 1.4+ type A connector', 'kicadSymbolki_fp_filters': 'HDMI*A*'}])
    newPart['name'].append('HDMI_A_1.4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

