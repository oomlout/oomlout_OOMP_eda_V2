
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "D1X8K-14BL"
    hexID = "SZKDICHARACTERD1X8K14BL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'D168K', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'D1X8K-14BL', 'kicadSymbolFootprint': 'Display_7Segment:D1X8K', 'kicadSymbolDatasheet': 'https://ia800903.us.archive.org/24/items/CTKD1x8K/Cromatek%20D168K.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment ultra bright blue LED, low current, common cathode', 'kicadSymbolki_fp_filters': 'D1X8K*'}])
    newPart['name'].append('D1X8K-14BL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

