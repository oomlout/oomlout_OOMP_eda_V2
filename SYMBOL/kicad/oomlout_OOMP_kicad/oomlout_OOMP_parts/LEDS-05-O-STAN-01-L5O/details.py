
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-05-O-STAN-01-L5O"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS5OSTAN1L5O"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-05-O-STAN-01-L5O', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-05-O-STAN-01-L5O', 'kicadSymbolDatasheet': 'oom.lt/L5O', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L5O;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-05-O-STAN-01-L5O')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

