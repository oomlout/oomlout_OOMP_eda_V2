
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS51363"
    hexID = "SZKREGULATORSWITCHINGTPS51363"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS51363', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_R-PWQFN-N28_EP2.1x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps51363.pdf', 'kicadSymbolki_keywords': 'Step-down', 'kicadSymbolki_description': 'High-voltage input, synchronous converter with integrated FET, QFN-28', 'kicadSymbolki_fp_filters': '*QFN*EP2.1x3.1mm*'}])
    newPart['name'].append('Regulator_Switching : TPS51363')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

