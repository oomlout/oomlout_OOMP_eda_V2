
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0805-Y-STAN-01-L85Y"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS85YSTAN1L85Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0805-Y-STAN-01-L85Y', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0805-Y-STAN-01-L85Y', 'kicadSymbolDatasheet': 'oom.lt/L85Y', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L85Y;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0805-Y-STAN-01-L85Y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

