
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSP-7503"
    hexID = "SZKDICHARACTERHDSP753"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HDSP-A153', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSP-7503', 'kicadSymbolFootprint': 'Display_7Segment:HDSP-A151', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-2553EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment high efficiency red, common cathode', 'kicadSymbolki_fp_filters': 'HDSP?A151*'}])
    newPart['name'].append('HDSP-7503')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

