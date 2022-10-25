
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0805-X-O220-01-R8O220-C17561"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE85XO221R8O22C17561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0805-X-O220-01-R8O220-C17561', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0805-X-O220-01-R8O220-C17561', 'kicadSymbolDatasheet': 'oom.lt/R8O220', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R8O220;PARTL C-JLCC;C17561;MANUF C-XXXX;0805W8F220JT5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : RESE-0805-X-O220-01-R8O220-C17561')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

