
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-08-RGB-FROS-WS2811-L8RGB21"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS8RGBFROSWS2811L8RGB21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-08-RGB-FROS-WS2811-L8RGB21', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-08-RGB-FROS-WS2811-L8RGB21', 'kicadSymbolDatasheet': 'oom.lt/L8RGB21', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L8RGB21;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-08-RGB-FROS-WS2811-L8RGB21')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

