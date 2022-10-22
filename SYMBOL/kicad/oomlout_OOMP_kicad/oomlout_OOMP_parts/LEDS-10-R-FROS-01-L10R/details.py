
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-10-R-FROS-01-L10R"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS1RFROS1L1R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-10-R-FROS-01-L10R', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-10-R-FROS-01-L10R', 'kicadSymbolDatasheet': 'oom.lt/L10R', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L10R;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-10-R-FROS-01-L10R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

