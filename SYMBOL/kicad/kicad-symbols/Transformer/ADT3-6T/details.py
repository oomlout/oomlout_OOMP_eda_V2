
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT3-6T"
    hexID = "SZKTRADT36T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT3-6T', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD636_H4.11mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT3-6T+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '1-600MHz 1:3 RF Transformer, Unbalanced to Balanced Center Tap, CD636', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD636*'}])
    newPart['name'].append('Transformer : ADT3-6T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

