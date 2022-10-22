
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "AD-121F2"
    hexID = "SZKDICHARACTERAD121F2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'AD-121F2', 'kicadSymbolFootprint': 'Display_7Segment:AD-121F2', 'kicadSymbolDatasheet': 'http://usasyck.com/products/AD-121F2_cat_e.pdf', 'kicadSymbolki_keywords': 'display RGB LED digit 7-segment', 'kicadSymbolki_description': 'Single Digit 7-segment RGB LED Display, 1-inch digit height, common anode', 'kicadSymbolki_fp_filters': 'AD*121F2*'}])
    newPart['name'].append('AD-121F2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

