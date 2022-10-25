
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0805-R-STAN-01-L85R"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS85RSTAN1L85R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0805-R-STAN-01-L85R', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0805-R-STAN-01-L85R', 'kicadSymbolDatasheet': 'oom.lt/L85R', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L85R;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0805-R-STAN-01-L85R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

