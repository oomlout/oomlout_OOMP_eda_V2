
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT1.5-17"
    hexID = "SZKTRADT1517"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT1.5-17', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD542_H2.84mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT1.5-17+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.5-1700MHz 1:1.5 RF Transformer, Unbalanced to Unbalanced, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD542*'}])
    newPart['name'].append('Transformer : ADT1.5-17')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

