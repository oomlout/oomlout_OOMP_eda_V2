
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0603-X-O183-01-R6O183-C25810"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE63XO1831R6O183C2581"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O183-01-R6O183-C25810', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O183-01-R6O183-C25810', 'kicadSymbolDatasheet': 'oom.lt/R6O183', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6O183;PARTL C-JLCC;C25810;MANUF C-XXXX;0603WAF1802T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0603-X-O183-01-R6O183-C25810')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

