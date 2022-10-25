
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "I386EX_PQFP"
    hexID = "SZKMCUINTELI386EXPQFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'I386EX_PQFP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': 'Intel I386EX Embedded microprocessor, PQFP-132', 'kicadSymbolki_fp_filters': 'PQFP*'}])
    newPart['name'].append('MCU_Intel : I386EX_PQFP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

