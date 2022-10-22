
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DC56-11YWA"
    hexID = "SZKDICHARACTERDC5611YWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DC56-11SYKWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DC56-11YWA', 'kicadSymbolFootprint': 'Display_7Segment:DA56-11SYKWA', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/DC56-11YWA.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double digit 7 segment yellow LED common cathode', 'kicadSymbolki_fp_filters': '*DA56*11*'}])
    newPart['name'].append('DC56-11YWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

