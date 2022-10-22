
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DA04-11CGKWA"
    hexID = "SZKDICHARACTERDA411CGKWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DA04-11CGKWA', 'kicadSymbolFootprint': 'Display_7Segment:DA04-11CGKWA', 'kicadSymbolDatasheet': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/DA04-11CGKWA(Ver.6A).pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double 7 segment green LED common anode', 'kicadSymbolki_fp_filters': '*DA04*11*'}])
    newPart['name'].append('DA04-11CGKWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

