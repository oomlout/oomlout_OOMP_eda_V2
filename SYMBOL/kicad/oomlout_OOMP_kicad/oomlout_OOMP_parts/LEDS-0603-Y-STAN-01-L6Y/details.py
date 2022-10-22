
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0603-Y-STAN-01-L6Y"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS63YSTAN1L6Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0603-Y-STAN-01-L6Y', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0603-Y-STAN-01-L6Y', 'kicadSymbolDatasheet': 'oom.lt/L6Y', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L6Y;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-0603-Y-STAN-01-L6Y')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

