
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-0603-X-O151-67-R6151A"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESE63XO15167R6151A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O151-67-R6151A', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O151-67-R6151A', 'kicadSymbolDatasheet': 'oom.lt/R6151A', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6151A;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0603-X-O151-67-R6151A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

