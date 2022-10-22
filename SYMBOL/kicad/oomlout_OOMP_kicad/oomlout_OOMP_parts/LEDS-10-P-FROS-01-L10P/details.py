
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-10-P-FROS-01-L10P"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS1PFROS1L1P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-10-P-FROS-01-L10P', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-10-P-FROS-01-L10P', 'kicadSymbolDatasheet': 'oom.lt/L10P', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L10P;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-10-P-FROS-01-L10P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

