
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-0603-W-STAN-01-L6W"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS63WSTAN1L6W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-0603-W-STAN-01-L6W', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-0603-W-STAN-01-L6W', 'kicadSymbolDatasheet': 'oom.lt/L6W', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L6W;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-0603-W-STAN-01-L6W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

