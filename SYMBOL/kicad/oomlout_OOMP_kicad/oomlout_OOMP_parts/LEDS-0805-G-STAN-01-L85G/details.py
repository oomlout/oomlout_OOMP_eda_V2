
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0805-G-STAN-01-L85G"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS85GSTAN1L85G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0805-G-STAN-01-L85G', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0805-G-STAN-01-L85G', 'kicadSymbolDatasheet': 'oom.lt/L85G', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L85G;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0805-G-STAN-01-L85G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

