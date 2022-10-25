
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "SD_Card"
    hexID = "SZKCNSDCARD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SD_Card', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://portal.fciconnect.com/Comergent//fci/drawing/10067847.pdf', 'kicadSymbolki_keywords': 'connector SD', 'kicadSymbolki_description': 'SD Card Reader', 'kicadSymbolki_fp_filters': 'SD*'}])
    newPart['name'].append('Connector : SD_Card')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

