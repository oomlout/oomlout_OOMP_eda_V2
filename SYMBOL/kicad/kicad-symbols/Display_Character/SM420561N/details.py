
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "SM420561N"
    hexID = "SZKDICHARACTERSM42561N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SM420561N', 'kicadSymbolFootprint': 'Display_7Segment:7SegmentLED_LTS6760_LTS6780', 'kicadSymbolDatasheet': 'https://datasheet.lcsc.com/szlcsc/Wuxi-ARK-Tech-Elec-SM420561N_C141367.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment blue LED, common cathode', 'kicadSymbolki_fp_filters': '7SegmentLED?LTS6760?LTS6780*'}])
    newPart['name'].append('SM420561N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

