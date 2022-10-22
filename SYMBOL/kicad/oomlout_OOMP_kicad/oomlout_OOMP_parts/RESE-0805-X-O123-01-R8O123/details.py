
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-0805-X-O123-01-R8O123"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESE85XO1231R8O123"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0805-X-O123-01-R8O123', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0805-X-O123-01-R8O123', 'kicadSymbolDatasheet': 'oom.lt/R8O123', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R8O123;PARTL C-JLCC;C17444;MANUF C-XXXX;0805W8F1202T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0805-X-O123-01-R8O123')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

