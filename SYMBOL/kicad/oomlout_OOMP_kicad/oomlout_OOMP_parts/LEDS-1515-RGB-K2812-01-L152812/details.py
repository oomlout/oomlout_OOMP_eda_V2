
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-1515-RGB-K2812-01-L152812"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS1515RGBK28121L152812"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-1515-RGB-K2812-01-L152812', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-1515-RGB-K2812-01-L152812', 'kicadSymbolDatasheet': 'oom.lt/L152812', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L152812;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-1515-RGB-K2812-01-L152812')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

