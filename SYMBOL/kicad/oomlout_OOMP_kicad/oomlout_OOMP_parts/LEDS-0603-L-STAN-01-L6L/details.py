
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0603-L-STAN-01-L6L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS63LSTAN1L6L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0603-L-STAN-01-L6L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0603-L-STAN-01-L6L', 'kicadSymbolDatasheet': 'oom.lt/L6L', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L6L;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-0603-L-STAN-01-L6L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

