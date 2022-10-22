
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-1206-X-O121-01-R12O121"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESE126XO1211R12O121"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-1206-X-O121-01-R12O121', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-1206-X-O121-01-R12O121', 'kicadSymbolDatasheet': 'oom.lt/R12O121', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R12O121;PARTL C-JLCC;C17909;MANUF C-XXXX;1206W4F1200T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-1206-X-O121-01-R12O121')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

