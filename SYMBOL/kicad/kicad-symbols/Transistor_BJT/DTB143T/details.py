
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "DTB143T"
    hexID = "SZKTRANSISTORBJTDTB143T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DTB143T', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'ROHM Digital PNP Transistor', 'kicadSymbolki_description': 'Digital PNP Transistor, 4k7/NONE, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23* SC?59*'}])
    newPart['name'].append('Transistor_BJT : DTB143T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

