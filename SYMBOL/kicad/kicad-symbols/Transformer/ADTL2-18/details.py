
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADTL2-18"
    hexID = "SZKTRADTL218"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADTL1-4-75', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADTL2-18', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD542_H2.84mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADTL2-18+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '30-1800MHz 1:2 RF Transformer, Balanced Transmission Line, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD542*'}])
    newPart['name'].append('Transformer : ADTL2-18')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

