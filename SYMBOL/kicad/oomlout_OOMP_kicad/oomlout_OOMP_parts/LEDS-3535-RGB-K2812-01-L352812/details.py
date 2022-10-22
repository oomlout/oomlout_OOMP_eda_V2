
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-3535-RGB-K2812-01-L352812"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS3535RGBK28121L352812"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-3535-RGB-K2812-01-L352812', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-3535-RGB-K2812-01-L352812', 'kicadSymbolDatasheet': 'oom.lt/L352812', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L352812;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-3535-RGB-K2812-01-L352812')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

