
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DA04-11EWA"
    hexID = "SZKDICHARACTERDA411EWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DA04-11SURKWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DA04-11EWA', 'kicadSymbolFootprint': 'Display_7Segment:DA04-11SURKWA', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/DA04-11EWA.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double 7 segment high efficient red LED common anode', 'kicadSymbolki_fp_filters': '*DA04*11*'}])
    newPart['name'].append('DA04-11EWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

