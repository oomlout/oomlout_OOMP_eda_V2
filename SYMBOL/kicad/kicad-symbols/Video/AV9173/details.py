
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "AV9173"
    hexID = "SZKVIDEOAV9173"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AV9173', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ibselectronics.com/ibsstore/datasheet/Others/AV9173-01CN08.pdf', 'kicadSymbolki_keywords': 'video pll', 'kicadSymbolki_description': 'Video Genlock PLL'}])
    newPart['name'].append('AV9173')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

