
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0402-X-O802-01-R4O802-C25917"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE42XO821R4O82C25917"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0402-X-O802-01-R4O802-C25917', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0402-X-O802-01-R4O802-C25917', 'kicadSymbolDatasheet': 'oom.lt/R4O802', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R4O802;PARTL C-JLCC;C25917;MANUF C-XXXX;0402WGF6801TCE;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0402-X-O802-01-R4O802-C25917')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

