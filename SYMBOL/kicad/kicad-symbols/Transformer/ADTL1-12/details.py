
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADTL1-12"
    hexID = "SZKTRADTL112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADTL1-4-75', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADTL1-12', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD542_H2.84mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADTL1-12+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '20-1200MHz 1:1 RF Transformer, Balanced Transmission Line, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD542*'}])
    newPart['name'].append('Transformer : ADTL1-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

