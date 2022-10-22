
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-10-L-FROS-01-L10L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS1LFROS1L1L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-10-L-FROS-01-L10L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-10-L-FROS-01-L10L', 'kicadSymbolDatasheet': 'oom.lt/L10L', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L10L;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-10-L-FROS-01-L10L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

