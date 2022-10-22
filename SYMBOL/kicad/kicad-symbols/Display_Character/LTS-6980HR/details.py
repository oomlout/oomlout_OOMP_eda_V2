
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "LTS-6980HR"
    hexID = "SZKDICHARACTERLTS698HR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'AFF', 'kicadSymbolValue': 'LTS-6980HR', 'kicadSymbolFootprint': 'Display_7Segment:7SegmentLED_LTS6760_LTS6780', 'kicadSymbolDatasheet': 'http://datasheet.octopart.com/LTS-6960HR-Lite-On-datasheet-11803242.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'DISPLAY 7 SEGMENTS common K, high efficient red', 'kicadSymbolki_fp_filters': '7SegmentLED?LTS6760?LTS6780*'}])
    newPart['name'].append('LTS-6980HR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

