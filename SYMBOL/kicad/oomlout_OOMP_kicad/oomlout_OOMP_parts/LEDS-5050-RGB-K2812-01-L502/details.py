
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-5050-RGB-K2812-01-L502"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS55RGBK28121L52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-5050-RGB-K2812-01-L502', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-5050-RGB-K2812-01-L502', 'kicadSymbolDatasheet': 'oom.lt/L502', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L502;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-5050-RGB-K2812-01-L502')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

