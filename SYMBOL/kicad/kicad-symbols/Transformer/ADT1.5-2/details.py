
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT1.5-2"
    hexID = "SZKTRADT152"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT1.5-2', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD636_H4.11mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT1.5-2+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.3-225MHz 1:1.5 RF Transformer, Balanced to Balanced, CD636', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD636*'}])
    newPart['name'].append('Transformer : ADT1.5-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

