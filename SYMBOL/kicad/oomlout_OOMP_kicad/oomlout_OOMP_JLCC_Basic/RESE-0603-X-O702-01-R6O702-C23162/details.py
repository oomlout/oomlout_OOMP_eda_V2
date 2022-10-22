
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0603-X-O702-01-R6O702-C23162"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE63XO721R6O72C23162"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O702-01-R6O702-C23162', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O702-01-R6O702-C23162', 'kicadSymbolDatasheet': 'oom.lt/R6O702', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6O702;PARTL C-JLCC;C23162;MANUF C-XXXX;0603WAF4701T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('RESE-0603-X-O702-01-R6O702-C23162')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

