
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-05-I9-STAN-01-L5I9"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS5I9STAN1L5I9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-05-I9-STAN-01-L5I9', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-05-I9-STAN-01-L5I9', 'kicadSymbolDatasheet': 'oom.lt/L5I9', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L5I9;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-05-I9-STAN-01-L5I9')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

