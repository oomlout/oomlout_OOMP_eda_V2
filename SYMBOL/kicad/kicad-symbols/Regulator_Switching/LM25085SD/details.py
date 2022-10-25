
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM25085SD"
    hexID = "SZKREGULATORSWITCHINGLM2585SD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM25085SD', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm25085.pdf', 'kicadSymbolki_keywords': 'buck switching controller', 'kicadSymbolki_description': '42V Constant On-Time PFET Buck Switching Controller, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x3mm*P0.5mm*EP1.6x2.0mm*'}])
    newPart['name'].append('Regulator_Switching : LM25085SD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

