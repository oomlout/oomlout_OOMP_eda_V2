
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DE114-RS-20"
    hexID = "SZKDICHARACTERDE114RS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DE114-RS-20', 'kicadSymbolFootprint': 'Display_7Segment:DE114-RS-20', 'kicadSymbolDatasheet': 'http://www.display-elektronik.de/filter/DE114-RS-20_635.pdf', 'kicadSymbolki_keywords': 'display LCD 7-segment', 'kicadSymbolki_description': '3 and half digit 7 segment reflective standard LCD with ~~ and BAT, pin length 6.35mm, -20°C to +70°C, 3V-5V VDD', 'kicadSymbolki_fp_filters': '*DE*114*RS*20*'}])
    newPart['name'].append('DE114-RS-20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

