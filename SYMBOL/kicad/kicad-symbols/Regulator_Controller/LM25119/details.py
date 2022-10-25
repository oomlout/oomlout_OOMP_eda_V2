
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LM25119"
    hexID = "SZKREGULATORCONTROLLERLM25119"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM25119', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm25119.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'Dual Synchronous Buck', 'kicadSymbolki_description': 'Wide Input Range, Dual Synchronous Buck Controller, WQFN-32', 'kicadSymbolki_fp_filters': 'WQFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Controller : LM25119')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

