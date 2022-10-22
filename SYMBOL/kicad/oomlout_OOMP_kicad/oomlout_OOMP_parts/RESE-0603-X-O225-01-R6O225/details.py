
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-0603-X-O225-01-R6O225"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESE63XO2251R6O225"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O225-01-R6O225', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O225-01-R6O225', 'kicadSymbolDatasheet': 'oom.lt/R6O225', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6O225;PARTL C-JLCC;C22938;MANUF C-XXXX;0603WAF2204T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0603-X-O225-01-R6O225')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

