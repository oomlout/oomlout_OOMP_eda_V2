
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-2020-RGB-K102-01-L20102"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS22RGBK121L212"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-2020-RGB-K102-01-L20102', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-2020-RGB-K102-01-L20102', 'kicadSymbolDatasheet': 'oom.lt/L20102', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L20102;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-2020-RGB-K102-01-L20102')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

