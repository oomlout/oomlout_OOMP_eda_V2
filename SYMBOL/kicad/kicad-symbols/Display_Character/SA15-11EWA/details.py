
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "SA15-11EWA"
    hexID = "SZKDICHARACTERSA1511EWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SA15-11SRWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SA15-11EWA', 'kicadSymbolFootprint': 'Display_7Segment:SA15-11xxx', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/SA15-11EWA.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'High Efficiency Red Single-digit Numeric Display with white white diffused lens, common anode', 'kicadSymbolki_fp_filters': 'SA15?11*'}])
    newPart['name'].append('SA15-11EWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

