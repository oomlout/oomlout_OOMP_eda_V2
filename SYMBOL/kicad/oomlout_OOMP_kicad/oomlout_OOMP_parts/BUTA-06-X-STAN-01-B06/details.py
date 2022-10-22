
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-06-X-STAN-01-B06"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA6XSTAN1B6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-06-X-STAN-01-B06', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-06-X-STAN-01-B06', 'kicadSymbolDatasheet': 'oom.lt/B06', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: B06;Push button switch, generic, two pins'}])
    newPart['name'].append('BUTA-06-X-STAN-01-B06')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

