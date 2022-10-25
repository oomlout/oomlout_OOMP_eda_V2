
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "DTB114G"
    hexID = "SZKTRANSISTORBJTDTB114G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DTB114G', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'ROHM Digital PNP Transistor', 'kicadSymbolki_description': 'Digital PNP Transistor, 0k/10k, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23* SC?59*'}])
    newPart['name'].append('Transistor_BJT : DTB114G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

