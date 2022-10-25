
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADTT1-6"
    hexID = "SZKTRADTT16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADTT1-6', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD637_H5.23mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADTT1-6+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.015-100MHz 1:1 RF Transformer, Unbalanced to Balanced Center Tap at Primary/Secondary, CD637', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD637*'}])
    newPart['name'].append('Transformer : ADTT1-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

