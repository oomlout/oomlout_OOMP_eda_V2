
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-2121-RGB-STAN-CA-LRGB2121CA"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS2121RGBSTANCALRGB2121CA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-2121-RGB-STAN-CA-LRGB2121CA', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-2121-RGB-STAN-CA-LRGB2121CA', 'kicadSymbolDatasheet': 'oom.lt/LRGB2121CA', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: LRGB2121CA;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-2121-RGB-STAN-CA-LRGB2121CA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

