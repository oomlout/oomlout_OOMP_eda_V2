
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DE122-XX-XX"
    hexID = "SZKDICHARACTERDE122XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DE122-XX-XX', 'kicadSymbolFootprint': 'Display_7Segment:DE122-XX-XX', 'kicadSymbolDatasheet': 'http://www.display-elektronik.de/filter/DE122-RS-20_635.pdf', 'kicadSymbolki_keywords': 'display LCD 7-segment', 'kicadSymbolki_description': '6 digit 7 segment reflective standard LCD, pin length 6.35mm, -20°C to +70°C, 3V-5V VDD', 'kicadSymbolki_fp_filters': 'DE122?XX?XX*'}])
    newPart['name'].append('DE122-XX-XX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

