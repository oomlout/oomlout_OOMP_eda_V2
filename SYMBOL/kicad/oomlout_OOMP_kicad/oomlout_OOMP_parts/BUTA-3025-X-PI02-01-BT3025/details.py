
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "BUTA-3025-X-PI02-01-BT3025"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSBUTA325XPI21BT325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'BUTA-3025-X-PI02-01-BT3025', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:BUTA-3025-X-PI02-01-BT3025', 'kicadSymbolDatasheet': 'oom.lt/BT3025', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button', 'kicadSymbolki_description': 'hexID: BT3025;Push button switch, generic, two pins'}])
    newPart['name'].append('BUTA-3025-X-PI02-01-BT3025')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

