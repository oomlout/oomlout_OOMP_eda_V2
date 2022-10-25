
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT2-71T"
    hexID = "SZKTRADT271T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADT1-6T', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT2-71T', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD637_H5.23mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT2-71T+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.40-500MHz 1:2 RF Transformer, Unbalanced to Balanced Center Tap, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD637*'}])
    newPart['name'].append('Transformer : ADT2-71T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

