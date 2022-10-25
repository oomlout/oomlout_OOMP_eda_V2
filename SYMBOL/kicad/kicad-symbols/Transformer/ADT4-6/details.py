
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT4-6"
    hexID = "SZKTRADT46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT4-6', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD637_H5.23mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT4-6+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.07-250MHz 1:4 RF Transformer, Balanced to Balanced, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD637*'}])
    newPart['name'].append('Transformer : ADT4-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

