
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0603-X-O434-01-R6O434-C25969"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE63XO4341R6O434C25969"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'R', 'kicadSymbolValue': 'RESE-0603-X-O434-01-R6O434-C25969', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:RESE-0603-X-O434-01-R6O434-C25969', 'kicadSymbolDatasheet': 'oom.lt/R6O434', 'kicadSymbolki_keywords': 'R res resistor', 'kicadSymbolki_description': 'hexID: R6O434;PARTL C-JLCC;C25969;MANUF C-XXXX;0603WAF4303T5E;Resistor', 'kicadSymbolki_fp_filters': 'R_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : RESE-0603-X-O434-01-R6O434-C25969')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

