
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_E3_SA6432"
    hexID = "SZKSWITCHSWE3SA6432"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SW_E3_SA3216', 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_E3_SA6432', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.e3-keys.com/files/SA%20Technical%20Datasheet%20v2.0.pdf', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button LCD', 'kicadSymbolki_description': 'Push button switch with LCD screen', 'kicadSymbolki_fp_filters': 'SW?PUSH?LCD?E3?SAxxxx*'}])
    newPart['name'].append('SW_E3_SA6432')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

