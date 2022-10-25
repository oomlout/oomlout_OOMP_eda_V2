
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-12-X-LEDS-01-B12L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA12XLS1B12L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-12-X-LEDS-01-B12L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-12-X-LEDS-01-B12L', 'kicadSymbolDatasheet': 'oom.lt/B12L', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: B12L;Push button switch, generic, two pins'}])
    newPart['name'].append('oomlout_OOMP_parts : BUTA-12-X-LEDS-01-B12L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

