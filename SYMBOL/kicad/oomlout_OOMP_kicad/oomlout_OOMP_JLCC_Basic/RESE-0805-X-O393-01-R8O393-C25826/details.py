
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0805-X-O393-01-R8O393-C25826"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE85XO3931R8O393C25826"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0805-X-O393-01-R8O393-C25826', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0805-X-O393-01-R8O393-C25826', 'kicadSymbolDatasheet': 'oom.lt/R8O393', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R8O393;PARTL C-JLCC;C25826;MANUF C-XXXX;0805W8F3902T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0805-X-O393-01-R8O393-C25826')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

