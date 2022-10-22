
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DA04-11GWA"
    hexID = "SZKDICHARACTERDA411GWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DA04-11CGKWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DA04-11GWA', 'kicadSymbolFootprint': 'Display_7Segment:DA04-11CGKWA', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/DA04-11GWA.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double 7 segment green LED common anode', 'kicadSymbolki_fp_filters': '*DA04*11*'}])
    newPart['name'].append('DA04-11GWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

