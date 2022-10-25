
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0805-L-STAN-01-L85L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS85LSTAN1L85L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0805-L-STAN-01-L85L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0805-L-STAN-01-L85L', 'kicadSymbolDatasheet': 'oom.lt/L85L', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L85L;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0805-L-STAN-01-L85L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

