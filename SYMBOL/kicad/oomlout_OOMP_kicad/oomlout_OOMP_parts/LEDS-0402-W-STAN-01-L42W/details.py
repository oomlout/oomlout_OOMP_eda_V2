
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0402-W-STAN-01-L42W"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS42WSTAN1L42W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0402-W-STAN-01-L42W', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0402-W-STAN-01-L42W', 'kicadSymbolDatasheet': 'oom.lt/L42W', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L42W;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0402-W-STAN-01-L42W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

