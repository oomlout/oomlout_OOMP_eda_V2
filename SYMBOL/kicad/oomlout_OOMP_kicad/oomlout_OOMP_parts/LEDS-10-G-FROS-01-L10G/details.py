
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-10-G-FROS-01-L10G"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLS1GFROS1L1G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-10-G-FROS-01-L10G', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-10-G-FROS-01-L10G', 'kicadSymbolDatasheet': 'oom.lt/L10G', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: L10G;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('oomlout_OOMP_parts : LEDS-10-G-FROS-01-L10G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

