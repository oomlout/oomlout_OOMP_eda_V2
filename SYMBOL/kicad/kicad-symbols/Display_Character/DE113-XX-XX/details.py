
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "DE113-XX-XX"
    hexID = "SZKDICHARACTERDE113XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DE113-XX-XX', 'kicadSymbolFootprint': 'Display_7Segment:DE113-XX-XX', 'kicadSymbolDatasheet': 'http://www.display-elektronik.de/filter/DE113-MS-20_75.pdf', 'kicadSymbolki_keywords': 'display LCD 7-segment', 'kicadSymbolki_description': '3 and half digit 7 segment transmissive standard LCD with LO BAT, pin length 7.5mm, -20°C to +70°C, 3V-5V VDD', 'kicadSymbolki_fp_filters': '*DE*113*'}])
    newPart['name'].append('DE113-XX-XX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

