
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-W04-X-O223-01-R4223"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESEW4XO2231R4223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-W04-X-O223-01-R4223', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-W04-X-O223-01-R4223', 'kicadSymbolDatasheet': 'oom.lt/R4223', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R4223;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-W04-X-O223-01-R4223')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

