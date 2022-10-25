
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BCX53"
    hexID = "SZKTRANSISTORBJTBCX53"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BCX51', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BCX53', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/bcx51_bcx52_bcx53.pdf', 'kicadSymbolki_keywords': 'PNP Transistor', 'kicadSymbolki_description': '1A Ic, 80V Vce, PNP Medium Power Transistor, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('Transistor_BJT : BCX53')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

