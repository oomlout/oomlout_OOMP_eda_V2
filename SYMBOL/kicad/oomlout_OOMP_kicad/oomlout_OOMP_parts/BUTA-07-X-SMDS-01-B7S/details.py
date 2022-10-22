
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-07-X-SMDS-01-B7S"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA7XSMS1B7S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-07-X-SMDS-01-B7S', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-07-X-SMDS-01-B7S', 'kicadSymbolDatasheet': 'oom.lt/B7S', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: B7S;Push button switch, generic, two pins'}])
    newPart['name'].append('BUTA-07-X-SMDS-01-B7S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

