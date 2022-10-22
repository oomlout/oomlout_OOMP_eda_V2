
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-08-RGB-STAN-CA-L8RGB"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS8RGBSTANCAL8RGB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-08-RGB-STAN-CA-L8RGB', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-08-RGB-STAN-CA-L8RGB', 'kicadSymbolDatasheet': 'oom.lt/L8RGB', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L8RGB;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-08-RGB-STAN-CA-L8RGB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

