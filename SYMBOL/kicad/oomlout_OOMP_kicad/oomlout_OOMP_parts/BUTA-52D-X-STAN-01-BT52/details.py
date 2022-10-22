
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-52D-X-STAN-01-BT52"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA52DXSTAN1BT52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-52D-X-STAN-01-BT52', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-52D-X-STAN-01-BT52', 'kicadSymbolDatasheet': 'oom.lt/BT52', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: BT52;Push button switch, generic, two pins'}])
    newPart['name'].append('BUTA-52D-X-STAN-01-BT52')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

