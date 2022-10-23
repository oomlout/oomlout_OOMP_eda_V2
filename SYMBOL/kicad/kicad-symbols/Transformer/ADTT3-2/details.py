
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADTT3-2"
    hexID = "SZKTRADTT32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADTT1.5-1', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADTT3-2', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD636_H4.11mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADTT3-2+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.2-210MHz 1:3 RF Transformer, Unbalanced to Balanced Center Tap at Primary/Secondary, CD636', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD636*'}])
    newPart['name'].append('ADTT3-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

