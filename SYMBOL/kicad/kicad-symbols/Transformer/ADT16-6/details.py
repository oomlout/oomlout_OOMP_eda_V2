
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ADT16-6"
    hexID = "SZKTRADT166"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADT1.5-2', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ADT16-6', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD636_H4.11mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADT16-6+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits RF Transformer', 'kicadSymbolki_description': '0.25-105MHz 1:16 RF Transformer, Balanced to Balanced, CD636', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD636*'}])
    newPart['name'].append('ADT16-6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

