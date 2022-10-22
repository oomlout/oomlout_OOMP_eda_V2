
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "SBC18-11EGWA"
    hexID = "SZKDICHARACTERSBC1811EGWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SBC18-11SURKCGKWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SBC18-11EGWA', 'kicadSymbolFootprint': 'Display_7Segment:SBC18-11SURKCGKWA', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/SBC18-11EGWA.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Single digit 7 segment hyper red and green LED display, common cathode', 'kicadSymbolki_fp_filters': '*SBC18*11*'}])
    newPart['name'].append('SBC18-11EGWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

