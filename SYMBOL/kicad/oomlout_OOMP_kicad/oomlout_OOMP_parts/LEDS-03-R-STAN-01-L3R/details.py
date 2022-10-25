
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-03-R-STAN-01-L3R"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS3RSTAN1L3R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-03-R-STAN-01-L3R', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-03-R-STAN-01-L3R', 'kicadSymbolDatasheet': 'oom.lt/L3R', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L3R;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-03-R-STAN-01-L3R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

