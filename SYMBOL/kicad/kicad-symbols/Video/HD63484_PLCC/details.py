
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "HD63484_PLCC"
    hexID = "SZKVIDEOHD63484PLCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HD63484_PLCC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ''}])
    newPart['name'].append('Video : HD63484_PLCC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

