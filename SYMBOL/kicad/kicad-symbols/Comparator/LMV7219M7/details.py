
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMV7219M7"
    hexID = "SZKCOMPARATORLMV7219M7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6561x-LT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV7219M7', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lmv7219.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single Low-Power High-Speed Push-Pull Output Comparator, SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Comparator : LMV7219M7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

