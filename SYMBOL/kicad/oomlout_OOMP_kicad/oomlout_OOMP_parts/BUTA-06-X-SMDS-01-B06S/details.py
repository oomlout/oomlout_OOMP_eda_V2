
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-06-X-SMDS-01-B06S"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA6XSMS1B6S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-06-X-SMDS-01-B06S', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-06-X-SMDS-01-B06S', 'kicadSymbolDatasheet': 'oom.lt/B06S', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: B06S;Push button switch, generic, two pins'}])
    newPart['name'].append('oomlout_OOMP_parts : BUTA-06-X-SMDS-01-B06S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

