
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "CC56-12SYKWA"
    hexID = "SZKDICHARACTERCC5612SYKWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CC56-12SYKWA', 'kicadSymbolFootprint': 'Display_7Segment:CA56-12SYKWA', 'kicadSymbolDatasheet': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/CC56-12SYKWA(Ver.6A).pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': '4 digit 7 segment super bright yellow LED, common cathode', 'kicadSymbolki_fp_filters': '*CA56*12SYKWA*'}])
    newPart['name'].append('CC56-12SYKWA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

