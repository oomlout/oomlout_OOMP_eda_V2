
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-6035-X-STAN-01-B6035"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA635XSTAN1B635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-6035-X-STAN-01-B6035', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-6035-X-STAN-01-B6035', 'kicadSymbolDatasheet': 'oom.lt/B6035', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: B6035;Push button switch, generic, two pins'}])
    newPart['name'].append('BUTA-6035-X-STAN-01-B6035')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

