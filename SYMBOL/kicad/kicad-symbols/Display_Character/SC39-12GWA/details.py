
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "SC39-12GWA"
    hexID = "SZKDICHARACTERSC3912GWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SC39-12EWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC39-12GWA', 'kicadSymbolFootprint': 'Display_7Segment:Sx39-1xxxxx', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/sc39-12gwa.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Single digit 7 segment display, green, common cathode', 'kicadSymbolki_fp_filters': 'S?39?1*'}])
    newPart['name'].append('SC39-12GWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

