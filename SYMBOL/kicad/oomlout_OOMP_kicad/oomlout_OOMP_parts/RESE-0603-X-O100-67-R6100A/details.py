
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "RESE-0603-X-O100-67-R6100A"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSRESE63XO167R61A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O100-67-R6100A', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O100-67-R6100A', 'kicadSymbolDatasheet': 'oom.lt/R6100A', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6100A;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('oomlout_OOMP_parts : RESE-0603-X-O100-67-R6100A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

