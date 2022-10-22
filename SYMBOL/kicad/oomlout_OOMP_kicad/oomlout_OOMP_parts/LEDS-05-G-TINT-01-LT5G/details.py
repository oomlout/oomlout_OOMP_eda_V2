
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-05-G-TINT-01-LT5G"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS5GTINT1LT5G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-05-G-TINT-01-LT5G', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-05-G-TINT-01-LT5G', 'kicadSymbolDatasheet': 'oom.lt/LT5G', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: LT5G;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-05-G-TINT-01-LT5G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

