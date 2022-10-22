
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0402-L-STAN-01-L42L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS42LSTAN1L42L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0402-L-STAN-01-L42L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0402-L-STAN-01-L42L', 'kicadSymbolDatasheet': 'oom.lt/L42L', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L42L;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-0402-L-STAN-01-L42L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

