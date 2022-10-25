
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "PBSS301PZ"
    hexID = "SZKTRANSISTORBJTPBSS31PZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PZT3906', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PBSS301PZ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PBSS301PZ.pdf', 'kicadSymbolki_keywords': 'PNP Transistor', 'kicadSymbolki_description': '-5.7A Ic, -12V Vce, Small Signal PNP Transistor, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_BJT : PBSS301PZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

