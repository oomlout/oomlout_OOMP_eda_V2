
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-W04-X-O331-01-R4331"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESEW4XO3311R4331"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-W04-X-O331-01-R4331', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-W04-X-O331-01-R4331', 'kicadSymbolDatasheet': 'oom.lt/R4331', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R4331;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-W04-X-O331-01-R4331')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

