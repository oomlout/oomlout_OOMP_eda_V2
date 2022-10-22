
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "LCD-016N002L"
    hexID = "SZKDICHARACTERLCD16N2L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LCD-016N002L', 'kicadSymbolFootprint': 'Display:LCD-016N002L', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/37299/37299.pdf', 'kicadSymbolki_keywords': 'display LCD dot-matrix', 'kicadSymbolki_description': 'LCD 12x2, 8 bit parallel bus, 3V or 5V VDD', 'kicadSymbolki_fp_filters': '*LCD*016N002L*'}])
    newPart['name'].append('LCD-016N002L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

