
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0805-X-O221-01-R8O221-C17557"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE85XO2211R8O221C17557"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0805-X-O221-01-R8O221-C17557', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0805-X-O221-01-R8O221-C17557', 'kicadSymbolDatasheet': 'oom.lt/R8O221', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R8O221;PARTL C-JLCC;C17557;MANUF C-XXXX;0805W8F2200T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0805-X-O221-01-R8O221-C17557')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

