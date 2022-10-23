
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADTT4-1"
    hexID = "SZKTRADTT41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADTT1.5-1', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADTT4-1', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD636_H4.11mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADTT4-1+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.2-120MHz 1:4 RF Transformer, Unbalanced to Balanced Center Tap at Primary/Secondary, CD636', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD636*'}])
    newPart['name'].append('ADTT4-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

