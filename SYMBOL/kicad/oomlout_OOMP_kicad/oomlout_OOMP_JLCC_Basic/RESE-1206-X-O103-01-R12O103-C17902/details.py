
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-1206-X-O103-01-R12O103-C17902"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE126XO131R12O13C1792"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-1206-X-O103-01-R12O103-C17902', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-1206-X-O103-01-R12O103-C17902', 'kicadSymbolDatasheet': 'oom.lt/R12O103', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R12O103;PARTL C-JLCC;C17902;MANUF C-XXXX;1206W4F1002T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-1206-X-O103-01-R12O103-C17902')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

